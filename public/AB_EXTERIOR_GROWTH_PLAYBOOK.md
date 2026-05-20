# AB Exterior Solutions Growth Playbook

## Goal

Build AB Exterior Solutions into a premium South Jersey exterior cleaning brand with three engines:

1. Local search visibility
2. Fast booking and reliable operations
3. Reviews, proof, and repeat customers

## Website Improvements Added

- Removed unsupported "number one" style claims so the brand feels credible.
- Added a clear 3-step booking process.
- Added South Jersey service-area content for local relevance.
- Added an FAQ section for customer trust and Google understanding.
- Added FAQ structured data.
- Added business hours structured data:
  - Monday-Friday: 8 AM-6 PM
  - Saturday: 8 AM-4 PM
  - Sunday: off
- Kept 2-hour booking windows so jobs have travel/setup buffer.

## Backend Booking Model

For now, the best workflow is:

1. Customer books a 2-hour slot.
2. Booking is saved in the backend.
3. Google Calendar checks if the slot is open.
4. If open, a pending event is added to the calendar.
5. Customer gets an email.
6. Austin/Sophia confirms the job.
7. Admin dashboard updates status.

This is more professional than instantly promising every job is final. Exterior work depends on weather, property condition, route timing, and job size.

## Google Growth Priorities

### Week 1

- Verify Google Business Profile.
- Add website, phone, services, hours, service areas, logo, and photos.
- Add every service with descriptions:
  - Pressure washing
  - Trash bin cleaning
  - Driveway cleaning
  - Patio cleaning
  - Sidewalk cleaning
  - Waste removal
  - Exterior cleaning packages
- Upload 10-20 real photos.
- Submit sitemap in Google Search Console.

### Weeks 2-4

- Ask every happy customer for a Google review.
- Reply to every review.
- Post 1 Google Business Profile update per week.
- Add before/after photos weekly.
- Add location/service pages as the business grows.

### Months 2-3

- Add separate pages for:
  - Pressure Washing Cherry Hill NJ
  - Trash Bin Cleaning Cherry Hill NJ
  - Pressure Washing Marlton NJ
  - Pressure Washing Voorhees NJ
  - Waste Removal South Jersey
- Add call tracking.
- Add Google Local Services Ads if pressure washing or a related category is available.
- Add a simple CRM pipeline for leads, estimates, booked jobs, completed jobs, and follow-up review requests.

## Operating Model

The best pressure washing businesses do not win only because they clean well. They win because they:

- Answer fast
- Show up on time
- Price clearly
- Capture before/after proof
- Ask for reviews
- Follow up after every job
- Build recurring customers
- Keep the schedule organized

## Sophia/Admin Role

Sophia should own:

- Checking new pending bookings
- Confirming schedule and job fit
- Texting customers when details are missing
- Updating booking status
- Asking for reviews after completed jobs
- Posting weekly photos/updates to Google Business Profile
- Tracking missed calls and unbooked leads

## Future Upgrade

When volume grows, move to a full CRM setup:

- Quote requests
- Deposits
- Route optimization
- SMS reminders
- Automated review requests
- Customer history
- Recurring trash-bin cleaning subscriptions

Recommended future stack:

- Next.js for the website
- Supabase for database/auth/admin
- Google Calendar integration
- Twilio or another SMS provider for reminders
- Stripe for deposits and subscriptions
