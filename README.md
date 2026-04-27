# 501c3 Grant Platform

Phase 1 full-stack shell for a nonprofit grant platform.

## Stack

- `frontend`: Next.js + TypeScript
- `backend`: FastAPI + SQLAlchemy
- `worker`: Python Redis worker
- `postgres`: PostgreSQL 16
- `redis`: Redis 7

## Local Development

1. Copy environment files if needed:
   - `frontend/.env.example` -> `frontend/.env`
   - `backend/.env.example` -> `backend/.env`
   - `worker/.env.example` -> `worker/.env`
2. Start everything:
   - `docker compose up --build`

## Service URLs

- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`
- Health check: `http://localhost:8000/health`

## What is implemented in Phase 1

- Bootable frontend homepage
- Backend `/health` endpoint
- Backend checks Postgres and Redis connectivity
- Worker heartbeat process connected to Redis
- Docker Compose orchestration with one command
- Basic CI for frontend and backend lint/build checks
