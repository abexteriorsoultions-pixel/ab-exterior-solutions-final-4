# AB Exterior Solutions Website

Professional responsive website for AB Exterior Solutions with booking, reviews, and an admin dashboard backed by SQLite.

The public site is built as one polished landing page in the same order as the design reference:

1. Hero
2. Services
3. Packages
4. Summer Refresh deal
5. Waste removal
6. Why AB Exterior
7. Gallery
8. Reviews
9. Booking/contact
10. Footer

## Run Locally

```bash
python3 server.py
```

Open `http://127.0.0.1:8000`.

Admin dashboard: `http://127.0.0.1:8000/admin.html`

Default local admin credentials:

- Username: `admin`
- Password: `admin123`

Set these before deployment:

```bash
ADMIN_USER="your-user" ADMIN_PASSWORD="your-password" SESSION_SECRET="long-random-secret" python3 server.py
```

## Backend

- Bookings save to `data/ab_exterior.db`
- New bookings can be sent to Google Calendar and email through a Google Apps Script webhook
- Reviews save to `data/ab_exterior.db`
- Admins can update booking status
- Admins can approve, hide, or delete reviews
- Only approved reviews show publicly

## Google Calendar Booking Automation

The backend is ready to send each new booking to Google Calendar and email. To turn it on:

1. Copy `.env.example` to `.env`.
2. Open `integrations/google-booking-webhook.gs` in Google Apps Script.
3. Replace `SHARED_SECRET`, `CALENDAR_ID`, and `OWNER_EMAIL`.
4. Deploy the script as a Web App with access set to receive website requests.
5. Paste the Web App URL into `BOOKING_WEBHOOK_URL` in `.env`.
6. Put the same private secret in `BOOKING_WEBHOOK_SECRET`.

After that, every booking still saves to the website database, and the webhook creates a Google Calendar event, emails the business, and emails the customer.

## Deployment Notes

This app is ready to connect behind a GoDaddy domain after deploying it to a server that can run Python. Point the domain DNS to the host, set the production environment variables, and run the app behind HTTPS.

For a future Supabase migration, move the `bookings` and `reviews` tables into Supabase, then replace the API database calls in `server.py` with Supabase client calls.

## Edit Public Business Info

Update `public/site-config.js` for:

- Phone number
- Email
- Service area
- Future domain
- Social links

After you buy the domain, replace:

```js
domain: "https://your-domain.com"
```

with your real website link.
