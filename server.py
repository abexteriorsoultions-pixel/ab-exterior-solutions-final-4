from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
import datetime as dt
import base64
import hashlib
import hmac
import json
import os
import secrets
import sqlite3
import time
import urllib.error
import urllib.request


ROOT = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(ROOT, "public")
DATA_DIR = os.environ.get("DATA_DIR", os.path.join(ROOT, "data"))
DB_PATH = os.environ.get("DB_PATH", os.path.join(DATA_DIR, "ab_exterior.db"))


def load_env_file():
    path = os.path.join(ROOT, ".env")
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env_file()

ADMIN_USER = os.environ.get("ADMIN_USER", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin123")
SESSION_SECRET = os.environ.get("SESSION_SECRET", "change-this-before-deployment")
BOOKING_WEBHOOK_URL = os.environ.get("BOOKING_WEBHOOK_URL", "")
BOOKING_WEBHOOK_SECRET = os.environ.get("BOOKING_WEBHOOK_SECRET", "")
BUSINESS_NOTIFICATION_EMAIL = os.environ.get("BUSINESS_NOTIFICATION_EMAIL", "info@abexteriorsolutions.com")
BOOKING_TIMEZONE = os.environ.get("BOOKING_TIMEZONE", "America/New_York")
DEFAULT_EVENT_DURATION_MINUTES = int(os.environ.get("DEFAULT_EVENT_DURATION_MINUTES", "120"))
BOOKING_BLOCK_MINUTES = int(os.environ.get("BOOKING_BLOCK_MINUTES", str(DEFAULT_EVENT_DURATION_MINUTES)))
ALLOWED_BOOKING_TIMES = {"8:00 AM", "10:00 AM", "12:00 PM", "2:00 PM", "4:00 PM"}


def parse_booking_start(value):
    text = clean(value)
    try:
        date_part, time_part = text.split(" ", 1)
        selected_date = dt.datetime.strptime(date_part, "%Y-%m-%d").date()
    except ValueError:
        return None

    if time_part not in ALLOWED_BOOKING_TIMES:
        return None

    try:
        selected_time = dt.datetime.strptime(time_part, "%I:%M %p").time()
    except ValueError:
        return None

    return dt.datetime.combine(selected_date, selected_time)


def booking_time_is_available(preferred_time):
    requested = parse_booking_start(preferred_time)
    if not requested:
        return False, "Please choose one of the available appointment times."

    today = dt.datetime.now().date()
    if requested.date() < today:
        return False, "Please choose a future appointment date."

    if requested.weekday() == 6:
        return False, "Online booking is available Monday through Saturday. Please choose another day."
    if requested.weekday() == 5 and requested.time() == dt.time(16, 0):
        return False, "Saturday online appointments are available from 8:00 AM to 4:00 PM. Please choose an earlier Saturday slot."

    requested_end = requested + dt.timedelta(minutes=BOOKING_BLOCK_MINUTES)
    with db() as con:
        rows = con.execute(
            """
            SELECT preferred_time FROM bookings
            WHERE status IN ('Pending', 'Confirmed')
            """
        ).fetchall()

    for row in rows:
        existing = parse_booking_start(row["preferred_time"])
        if not existing:
            continue
        existing_end = existing + dt.timedelta(minutes=BOOKING_BLOCK_MINUTES)
        if requested < existing_end and requested_end > existing:
            return False, "That appointment time is already booked. Please choose another two-hour slot."

    return True, ""


def db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with db() as con:
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                service TEXT NOT NULL,
                preferred_time TEXT NOT NULL,
                message TEXT,
                status TEXT NOT NULL DEFAULT 'Pending',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                rating INTEGER NOT NULL,
                review TEXT NOT NULL,
                service TEXT,
                status TEXT NOT NULL DEFAULT 'Pending',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def read_json(handler):
    length = int(handler.headers.get("Content-Length", 0))
    raw = handler.rfile.read(length).decode("utf-8") if length else "{}"
    return json.loads(raw or "{}")


def send_json(handler, payload, status=HTTPStatus.OK):
    body = json.dumps(payload).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def clean(value):
    return str(value or "").strip()


def booking_payload(booking_id, fields):
    return {
        "secret": BOOKING_WEBHOOK_SECRET,
        "booking_id": booking_id,
        "company": "AB Exterior Solutions",
        "business_email": BUSINESS_NOTIFICATION_EMAIL,
        "timezone": BOOKING_TIMEZONE,
        "duration_minutes": DEFAULT_EVENT_DURATION_MINUTES,
        "created_at": dt.datetime.now(dt.UTC).isoformat(),
        **fields,
    }


def notify_booking(booking_id, fields):
    if not BOOKING_WEBHOOK_URL:
        return {"enabled": False, "ok": False}

    body = json.dumps(booking_payload(booking_id, fields)).encode(""utf-8"")