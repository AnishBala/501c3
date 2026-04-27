import redis

from app.config import settings


def get_redis_client() -> redis.Redis:
    return redis.from_url(settings.redis_url, decode_responses=True)


def check_redis_connection() -> bool:
    client = get_redis_client()
    return bool(client.ping())
