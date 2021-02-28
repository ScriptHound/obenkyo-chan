from typing import Any
import redis

EXPIRATION_TIMEOUT = 120


class Cache:
    def __init__(self) -> None:
        self.__redis = redis.Redis(host='redis', port=6379, db=0)

    def set(self, key: Any, value: Any) -> None:
        self.__redis.set(key, value)
        self.__redis.expire(key, EXPIRATION_TIMEOUT)

    def get(self, key: Any) -> Any:
        return self.__redis.get(key)

cache = Cache()
