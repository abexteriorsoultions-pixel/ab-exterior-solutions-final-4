# Simple Deployment Steps

## Best Setup

Use Render as the all-in-one official website because it can run:

- The public website
- The booking backend
- The admin dashboard
- Reviews
- Google Calendar booking sync
- The SQLite database

Netlify is fine for a public front page, but it does not run this Python backend by itself.

## Files To Use

### Render / Full Website + Backend

Use:

```txt
ABExteriorSolutions-PRO-GROWTH-BACKEND-v4-CONTENTS.zip
```

Unzip it. Upload the files inside the zip to GitHub so the GitHub repo front page shows:

```txt
server.py
render.yaml
requirements.txt
public
integrations
README.md
DEPLOYMENT_GUIDE.md
GOOGLE_CALENDAR_SETUP.md
BACKEND_CALENDAR_BOOKING_SETUP.md
AB_EXTERIOR_GROWTH_PLAYBOOK.md
```

Do not upload the zip as the only file in GitHub. Render needs to see `server.py` and `render.yaml`.

### Netlify / Public Front Page Only

Use:

```txt
NETLIFY-PRO-GROWTH-v4-UNDER-10MB.zip
```

Upload it to Netlify under:

```txt
Site dashboard > Deploys > Drag and drop deploy
```

## Render Step By Step

1. Go to Render.
2. Click **New**.
3. Choose **Web Service**.
4. Connect your GitHub repo.
5. Choose your AB Exterior Solutions repo.
6. Use these settings:

```txt
Language: Python 3
Branch: main
Root Directory: leave blank
Build Command: python -m py_compile server.py
Start Command: python server.py
```

7. Add environment variables:

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
DATA_DIR=/var/data
```

8. Deploy.
9. When it is live, Render gives you a URL like:

```txt
https://ab-exterior-solutions.onrender.com
```

10. Test:

```txt
/api/health
/admin.html
```

## Google Apps Script Step By Step

1. Open Google Apps Script.
2. Paste the full code from:

```txt
integrations/google-booking-webhook.gs
```

3. Deploy as a web app.
4. Use:

```txt
Execute as: Me
Who has access: Anyone
```

5. Copy the web app URL.
6. Put that URL into Render as:

```txt
BOOKING_WEBHOOK_URL
```

## Domain Recommendation

Once Render is working, use Render as the official website if you want everything in one place.

If your domain is currently pointed to Netlify, you can keep Netlify live for now. When Render is fully working, switch the domain from Netlify to Render.

## Updating Later

When you want edits:

1. Tell Codex what to change.
2. Codex edits the files.
3. Codex makes a new zip.
4. Upload the new files to GitHub.
5. Render redeploys automatically.

For Netlify-only edits:

1. Codex makes a new under-10MB zip.
2. Go to Netlify > Deploys.
3. Drag the new zip into the deploy box.
