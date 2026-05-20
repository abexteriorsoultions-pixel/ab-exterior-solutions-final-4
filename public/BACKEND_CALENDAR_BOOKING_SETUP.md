# AB Exterior Solutions Backend + Google Calendar Booking

This setup is for the finished booking flow:

1. Customer chooses a service, date, and 2-hour appointment block.
2. The website backend saves the booking.
3. The backend sends the booking to Google Apps Script.
4. Google Apps Script checks your Google Calendar.
5. If the time is open, it creates a pending calendar event and emails both AB Exterior Solutions and the customer.
6. If the time is already booked, the customer is asked to choose another slot.

## Appointment Slots

Online booking uses these 2-hour blocks:

- 8:00 AM - 10:00 AM
- 10:00 AM - 12:00 PM
- 12:00 PM - 2:00 PM
- 2:00 PM - 4:00 PM
- 4:00 PM - 6:00 PM

Sunday online booking is blocked.

## Render Environment Variables

Add these to Render:

```txt
ADMIN_USER=admin
ADMIN_PASSWORD=make-a-strong-password
SESSION_SECRET=make-a-long-random-secret
BOOKING_WEBHOOK_URL=your-google-apps-script-web-app-url
BOOKING_WEBHOOK_SECRET=ABsolutions2026!
BUSINESS_NOTIFICATION_EMAIL=austin@abexteriorsolutions.com
BOOKING_TIMEZONE=America/New_York
DEFAULT_EVENT_DURATION_MINUTES=120
BOOKING_BLOCK_MINUTES=120
```

## Google Apps Script

Paste the full file from:

```txt
integrations/google-booking-webhook.gs
```

Then deploy it as a web app:

- Execute as: Me
- Who has access: Anyone

Copy the deployment URL into Render as `BOOKING_WEBHOOK_URL`.

## Admin / Sophia Workflow

Calendar events are created as pending holds. Sophia or an admin can:

- Check the job details in Google Calendar
- Contact the customer if needed
- Log into the AB Exterior admin dashboard
- Change booking status to Confirmed, Completed, or Canceled

This keeps the customer booking experience fast while still giving the business final control.
