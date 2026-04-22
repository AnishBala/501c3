# Grant Platform Build Plan for Cursor

## Goal

Build a web platform for nonprofits that helps them:

- search grants
- save and organize grants
- score grant fit
- create application workspaces
- paste grant prompts and draft answers
- run review checks on those drafts
- track submissions and outcomes

This plan is intentionally code-focused. It is written to be used as a direct implementation roadmap inside Cursor.

---

# Phase 1: Project Setup and App Skeleton

## Build
- Create a monorepo or clean repo structure with:
  - `frontend/`
  - `backend/`
  - `worker/`
- Set up:
  - Next.js + TypeScript frontend
  - Python FastAPI backend
  - PostgreSQL database
  - Redis for background jobs
- Add Docker Compose for local development
- Add `.env` handling for all services
- Add basic CI config
- Add linting and formatting:
  - frontend: ESLint + Prettier
  - backend: Ruff + Black

## Code Requirements
- Frontend should boot to a working homepage
- Backend should boot with a `/health` endpoint
- Database should connect successfully
- Redis should connect successfully
- Worker process should start successfully

## Completion Check
This phase is complete when:
- all services run locally with one command
- frontend loads in browser
- backend health route returns success
- backend can talk to Postgres
- worker can connect to Redis

## Expected App State
A blank but working full-stack shell exists.

---

# Phase 2: Authentication and Organization Scoping

## Build
- Add authentication
- Add organization workspace support
- Add user roles:
  - owner
  - admin
  - editor
  - viewer
- Add protected routes on frontend
- Add auth middleware on backend
- Add database tables for:
  - users
  - organizations
  - organization_members

## Code Requirements
- Users can sign up and sign in
- A user can create an organization
- A user can invite another user
- Every backend query must be scoped to organization
- No cross-org data leaks

## Completion Check
This phase is complete when:
- a user can register
- a user can log in
- a user can create an org
- invited members can join
- org A cannot access org B data

## Expected App State
Users can access a protected dashboard inside an organization workspace.

---

# Phase 3: Database Schema and Core Models

## Build
Create database models and migrations for:

- users
- organizations
- organization_members
- grants
- grant_sources
- saved_grants
- applications
- application_prompts
- application_responses
- review_runs
- review_issues
- submission_records
- documents
- notifications

## Code Requirements
- Add migrations
- Add seed scripts with sample grant data
- Add created_at and updated_at fields to all tables
- Add soft delete only where needed
- Add indexes on:
  - grant deadline
  - organization_id
  - full text searchable fields
  - foreign keys

## Completion Check
This phase is complete when:
- all migrations run cleanly
- seed scripts populate usable test data
- backend models match schema
- test queries return valid records

## Expected App State
The app has a stable database foundation.

---

# Phase 4: Grant Ingestion Pipeline

## Build
Create the service that pulls grant data into the database.

## Sources
Start with:
- public APIs if available
- manually loaded JSON or CSV seed data
- scraper-ready source connectors for later extension

## Code Requirements
- Build a backend ingestion module
- Build a normalization layer that maps raw source data into the `grants` schema
- Build duplicate detection
- Store source URL and source name
- Store last refreshed timestamp
- Mark expired grants
- Add worker jobs for scheduled ingestion

## Suggested Software for This Phase
- Python
- requests or httpx
- BeautifulSoup or Playwright for future scraping
- pandas for cleaning if needed
- Celery or RQ for jobs

## Completion Check
This phase is complete when:
- backend can ingest grant records into DB
- duplicate grants are blocked or merged
- expired grants are marked correctly
- data refresh jobs run from worker

## Expected App State
The database contains real or realistic grant listings.

---

# Phase 5: Grant Search API

## Build
Create backend API routes for grant discovery.

## Routes
- `GET /grants`
- `GET /grants/:id`
- `POST /grants/save`
- `DELETE /grants/save/:id`
- `GET /grants/saved`

## Filters
Support:
- keyword search
- geography
- mission area
- deadline range
- funding range
- rolling vs fixed deadline
- eligibility type

## Code Requirements
- Add pagination
- Add sorting:
  - relevance
  - deadline
  - funding amount
- Add search indexes
- Return clean response objects
- Enforce org scoping for saved grants

## Completion Check
This phase is complete when:
- users can query grants with filters
- users can open a single grant
- users can save and unsave grants
- saved grants persist per organization

## Expected App State
Backend grant discovery functionality is complete.

---

# Phase 6: Grant Search Frontend

## Build
Create the frontend grant browsing experience.

## Pages
- dashboard
- grant search page
- grant detail page
- saved grants page

## Components
- search bar
- filters panel
- grant cards
- pagination controls
- save button
- grant detail panel
- empty states
- loading states
- error states

## Code Requirements
- Use typed API hooks
- Use optimistic UI for save/unsave if stable
- Show clear deadline and funding info
- Show source link
- Show grant summary
- Handle no-result cases cleanly

## Completion Check
This phase is complete when:
- user can search grants visually
- filters work
- saved grants appear in saved page
- detail view is fully functional

## Expected App State
The app is now demoable as a grant discovery platform.

---

# Phase 7: Organization Profile and Fit Inputs

## Build
Create an organization profile system used for fit scoring.

## Fields
- mission areas
- geography served
- nonprofit type
- annual budget range
- program categories
- target populations
- preferred grant size
- grants to avoid
- notes

## Code Requirements
- Add profile edit UI
- Add backend endpoints for org profile
- Validate inputs
- Persist structured data in DB
- Make data available to scoring engine

## Completion Check
This phase is complete when:
- org can fill out its profile
- profile data is stored correctly
- profile data can be read by backend services

## Expected App State
The app has the inputs needed for basic recommendation logic.

---

# Phase 8: Grant Fit Scoring Engine

## Build
Create a rule-based scoring service that compares an organization profile to a grant.

## Score Dimensions
- eligibility fit
- mission alignment
- geography alignment
- funding range fit
- deadline feasibility
- complexity or effort estimate

## Output
Return:
- overall score
- sub scores
- reasons
- warnings
- recommendation tag:
  - strong fit
  - possible fit
  - weak fit

## Code Requirements
- Build scoring logic in backend or worker service
- Keep rules readable and configurable
- Store score snapshots for saved grants
- Recalculate scores when org profile changes

## Completion Check
This phase is complete when:
- a saved grant can show a fit score
- score reasons are visible to user
- score recalculation works after org profile edits

## Expected App State
The app helps users decide which grants are worth pursuing.

---

# Phase 9: Application Workspace

## Build
Let users convert a saved grant into an active application workspace.

## Features
- create application from saved grant
- application title
- application status
- internal notes
- owner assignment
- due date
- related documents

## Prompt and Draft Storage
- add grant prompts/questions
- add draft responses
- edit responses
- autosave responses

## Code Requirements
- Create application routes
- Create prompt/response tables
- Add application detail page
- Add status transitions:
  - not started
  - in progress
  - review needed
  - ready to submit
  - submitted

## Completion Check
This phase is complete when:
- a user can turn a saved grant into an application
- prompts can be entered
- draft answers can be stored and edited
- application status updates correctly

## Expected App State
The app is now a real workflow tool, not just a search tool.

---

# Phase 10: Document Uploads

## Build
Add support for relevant files.

## Supported Use Cases
- upload grant guidelines
- upload budgets
- upload supporting documents
- attach files to applications

## Code Requirements
- Add file upload endpoint
- Store files in object storage
- Store metadata in DB
- Attach files to applications
- Restrict file access by organization
- Validate file size and type

## Suggested Software for This Phase
- S3 or Supabase Storage
- signed URLs
- antivirus scanning if needed later

## Completion Check
This phase is complete when:
- users can upload files
- uploaded files appear inside application workspace
- files are secure and scoped correctly

## Expected App State
Applications can now hold the materials users actually work with.

---

# Phase 11: Review Engine for Draft Checking

## Build
Create the core review system that checks draft answers against grant prompts.

## Input
- grant prompt text
- user draft answer
- optional organization preferences

## Output
- issue list
- category scores
- revision suggestions
- readiness label

## Review Categories
- prompt coverage
- specificity
- measurable outcomes
- clarity
- consistency
- missing evidence
- tone and structure
- unanswered sections

## Code Requirements
Build this in two layers.

### Layer 1: Deterministic checks
- empty answer
- short answer
- missing required sections
- obvious word count problems
- date mismatch
- number mismatch if detectable

### Layer 2: AI review
- whether answer addresses prompt
- whether answer is vague
- whether outcomes are measurable
- whether answer sounds unsupported
- whether answer needs more specificity

## Technical Requirements
- AI responses must be structured JSON
- Review results must be saved
- Users must be able to re-run reviews
- Never overwrite draft text automatically

## Completion Check
This phase is complete when:
- a user can run review on draft content
- issue list appears in UI
- review results persist
- user can compare multiple review runs

## Expected App State
This is the first real differentiation layer of the product.

---

# Phase 12: Budget Consistency Checks

## Build
Add structured budget support and compare it against narrative content.

## Features
- budget line item entry
- budget upload via CSV
- budget justification notes
- mismatch warnings

## Warning Types
- budget exceeds grant max
- narrative promises activities not budgeted
- budget includes unexplained items
- staffing levels appear unrealistic
- evaluation mentioned in narrative but not budgeted

## Code Requirements
- Create budget tables
- Parse CSV uploads
- Link budgets to applications
- Add rule-based checks
- Show warnings in UI

## Suggested Software for This Phase
- CSV parser
- pandas or native parsing
- openpyxl later only if XLSX is needed

## Completion Check
This phase is complete when:
- user can add a budget
- system can flag narrative-budget mismatches
- warnings display clearly

## Expected App State
The app now catches common structural problems.

---

# Phase 13: Submission Tracker

## Build
Track the lifecycle of grant applications.

## Fields
- submission date
- decision date
- status
- requested amount
- awarded amount
- rejection reason
- reviewer feedback
- internal lesson learned

## Statuses
- drafting
- submitted
- awarded
- rejected
- closed

## Code Requirements
- CRUD routes for submission records
- timeline or history view
- filters by status
- link records to applications

## Completion Check
This phase is complete when:
- submitted applications can be tracked
- outcomes can be logged
- historical records can be searched later

## Expected App State
Users can build institutional memory around grant work.

---

# Phase 14: Notifications and Reminders

## Build
Add operational reminders.

## Notifications
- upcoming deadline
- stale application
- assigned review needed
- review finished
- submission decision follow-up

## Code Requirements
- notification table
- in-app notifications
- email notifications
- scheduled jobs for reminders
- mark as read support

## Suggested Software for This Phase
- Resend, Postmark, or SendGrid
- worker scheduler

## Completion Check
This phase is complete when:
- reminders fire automatically
- users can see notifications in app
- deadline warnings work

## Expected App State
The app becomes operationally useful day to day.

---

# Phase 15: Admin Data Controls

## Build
Create internal tools for managing grant data quality.

## Features
- view ingested grants
- mark grants stale
- edit normalized data
- merge duplicates
- inspect ingestion failures
- re-run ingestion jobs

## Code Requirements
- admin-only routes
- admin-only frontend pages
- job status logging
- grant moderation actions

## Completion Check
This phase is complete when:
- an admin can fix bad grant records
- ingestion errors are visible
- duplicate cleanup is possible without DB manual edits

## Expected App State
The system is maintainable.

---

# Phase 16: Hardening and Production Readiness

## Build
Make the app safe and stable enough to deploy.

## Code Requirements
- role-based permission checks everywhere
- request validation everywhere
- rate limiting
- structured backend logging
- error tracking
- retry logic for failed jobs
- database backups
- loading states and error boundaries in frontend
- test coverage on critical flows

## Critical Flows to Test
- auth and org scoping
- grant search
- save and unsave grant
- create application
- upload file
- run review
- submission tracking
- notifications

## Suggested Software for This Phase
- Playwright
- pytest
- Sentry
- managed Postgres backups
- managed Redis if deployed

## Completion Check
This phase is complete when:
- core flows are tested
- no major auth leaks exist
- background jobs recover from failure
- app can survive basic production use

## Expected App State
The app is production-ready.

---

# Phase 17: Deployment

## Build
Deploy the full stack.

## Deployment Targets
- frontend: Vercel
- backend: Render, Railway, Fly.io, or AWS
- DB: managed Postgres
- Redis: managed Redis
- storage: S3 or equivalent

## Code Requirements
- production env config
- secure secrets handling
- migration on deploy strategy
- domain and SSL
- staging and production environments

## Completion Check
This phase is complete when:
- frontend is live
- backend is live
- DB migrations work in production
- file uploads work in production
- worker jobs run in production

## Expected App State
The platform is live and usable.

---

# Final Build Order Summary

Build in this exact order:

1. project setup
2. auth and org scoping
3. database schema
4. grant ingestion pipeline
5. grant search API
6. grant search frontend
7. org profile inputs
8. fit scoring
9. application workspace
10. document uploads
11. review engine
12. budget consistency checks
13. submission tracker
14. notifications
15. admin tools
16. hardening
17. deployment

---

# Final Definition of Done

The platform is complete when a nonprofit can:

- log in
- create an organization workspace
- search a live grant catalog
- save grants
- see fit scores
- create an application from a saved grant
- upload related documents
- paste prompts and draft answers
- run a review check
- get issue flags and revision guidance
- add a budget and get consistency warnings
- mark an application submitted
- track the result later
- receive deadline reminders

If any of that flow is missing, the platform is not done.
