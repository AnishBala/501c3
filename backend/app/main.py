from fastapi import FastAPI

from app.config import settings
from app.db import check_db_connection
from app.redis_client import check_redis_connection

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health() -> dict[str, object]:
    db_ok = False
    redis_ok = False
    errors: list[str] = []

    try:
        db_ok = check_db_connection()
    except Exception as exc:  # pragma: no cover
        errors.append(f"database: {exc}")

    try:
        redis_ok = check_redis_connection()
    except Exception as exc:  # pragma: no cover
        errors.append(f"redis: {exc}")

    return {
        "status": "ok" if db_ok and redis_ok else "degraded",
        "database": db_ok,
        "redis": redis_ok,
        "errors": errors,
    }
