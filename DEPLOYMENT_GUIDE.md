# Make ABExteriorSolutions.com Official

The website is ready for hosting. The easiest setup is:

1. Put this project on GitHub.
2. Deploy it on Render.
3. Point GoDaddy DNS to Render.

Do not put `http://127.0.0.1:8005` into GoDaddy. That is only your local preview.

## Step 1: GitHub

Create a private GitHub repository named `ab-exterior-solutions`.

Upload this project folder, but do not upload `.env` or `data/ab_exterior.db`.

The `.gitignore` file already protects those private/local files.

## Step 2: Render

1. Go to Render.
2. Create a new Blueprint or Web Service from the GitHub repo.
3. Use the included `render.yaml` if Render asks for a blueprint.
4. Add these environment variables in Render:

```bash
ADMIN_USER=choose-an-admin-username
ADMIN_PASSWORD=choose-a-strong-admin-password
SESSION_SECRET=make-this-a-long-random-private-value
BOOKING_WEBHOOK_URL=https://script.google.com/macros/s/AKfycbzUTVEZMvyCVLaKMtEIBhMfW5KLjrtef-y3nkmgqlylfWdhaeT-9KtCAYUeAMWtAcKe/exec
BOOKING_WEBHOOK_SECRET=ABsolutions2026!
BUSINESS_NOTIFICATION_EMAIL=austin@abexteriorsolutions.com
BOOKING_TIMEZONE=America/New_York
DEFAULT_EVENT_DURATION_MINUTES=60
```

Render should use:

```bash
Build command: python -m py_compile server.py
Start command: python server.py
```

After deployment, Render gives you a temporary URL like:

```txt
https://ab-exterior-solutions.onrender.com
```

## Step 3: GoDaddy Domain

In Render, add these custom domains:

```txt
ABExteriorSolutions.com
www.ABExteriorSolutions.com
```

Render will show DNS records. Go to GoDaddy DNS and add the exact records Render gives you.

Usually this means:

- `www` gets a `CNAME` record pointing to Render.
- The root domain gets an `A`, `ALIAS`, or similar record depending on what Render shows.

Use Render's exact values over any example.

## Step 4: Test

Once DNS verifies, test:

```txt
https://ABExteriorSolutions.com
https://ABExteriorSolutions.com/admin.html
```

Submit one test booking only when you are ready for it to create a real Google Calendar event and send emails.
