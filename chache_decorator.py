import functools
import time

def cache_data(timeout: int):
    """Simple caching decorator to cache function results for a given timeout in seconds."""
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            if key in cache:
                result, timestamp = cache[key]
                if (time.time() - timestamp) < timeout:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result
        return wrapper
    return decorator
