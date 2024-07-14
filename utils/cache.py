from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=300)


def get_from_cache(key: str):
    return cache.get(key)


def set_in_cache(key: str, value):
    cache[key] = value
