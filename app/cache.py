import redis
import json
from typing import Optional, Any
from .config import settings

class CacheService:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            decode_responses=True
        )

    def get(self, key: str) -> Optional[Any]:
        """Retrieve data from cache."""
        data = self.redis_client.get(key)
        if data:
            return json.loads(data)
        return None

    def set(self, key: str, value: Any, expire: int = settings.cache_expire_seconds):
        """Store data in cache with an expiration time."""
        self.redis_client.set(key, json.dumps(value), ex=expire)

cache_service = CacheService()
