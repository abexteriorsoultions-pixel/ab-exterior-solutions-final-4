# Google Calendar Booking Setup

This is the copy/paste setup for sending AB Exterior Solutions bookings into Google Calendar and email.

## 1. Create the Google Script

1. Go to `script.google.com`.
2. Start a new project.
3. Delete the starter code.
4. Paste everything from `integrations/google-booking-webhook.gs`.
5. Change these settings at the top:

```js
const SETTINGS = {
  SHARED_SECRET: "ab-exterior-change-this-secret",
  CALENDAR_ID: "primary",
  OWNER_EMAIL: "austin@abexteriorsolutions.com",
  COMPANY_NAME: "AB Exterior Solutions",
  TIMEZONE: "America/New_York",
  DEFAULT_START_HOUR: 9,
  DEFAULT_EVENT_MINUTES: 60,
};
```

Use a private phrase for `SHARED_SECRET`, such as `AB-Exterior-2026-private-booking-key`.

## 2. Deploy It

1. Click Deploy.
2. Choose Web app.
3. Run as: Me.
4. Access: Anyone.
5. Authorize Google Calendar and Gmail/Mail permissions.
6. Copy the Web app URL.

## 3. Connect the Website

Create a `.env` file beside `server.py` and add:

```bash
BOOKING_WEBHOOK_URL="PASTE-YOUR-GOOGLE-WEB-APP-URL-HERE"
BOOKING_WEBHOOK_SECRET="PASTE-THE-SAME-SECRET-HERE"
BUSINESS_NOTIFICATION_EMAIL="austin@abexteriorsolutions.com"
BOOKING_TIMEZONE="America/New_York"
DEFAULT_EVENT_DURATION_MINUTES=60
```

Restart the website server after saving `.env`.

## What Happens After Setup

When a customer books:

- The booking saves in the website admin dashboard.
- A Google Calendar event is created.
- The business receives an email with booking details.
- The customer receives a confirmation email.
