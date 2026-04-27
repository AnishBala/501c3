import os
import time

import redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


def run() -> None:
    client = redis.from_url(REDIS_URL, decode_responses=True)
    while True:
        try:
            client.ping()
            print("worker heartbeat: redis connection ok", flush=True)
        except Exception as exc:
            print(f"worker heartbeat: redis connection failed: {exc}", flush=True)
        time.sleep(10)


if __name__ == "__main__":
    run()
