#!/usr/bin/env python3
'''This module defines the Cache class with some decorators and functions.'''
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count how many times methods of the Cache class are called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Call a method that stores the history of inputs and outputs
       for a particular function.
    """
    key = method.__qualname__
    input_list_key = key + ':inputs'
    output_list_key = key + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(input_list_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_list_key, output)
        return output

    return wrapper


def replay(method):
    """Display the history of calls of `method`."""
    redis = method.__self__._redis
    qualified_name = method.__qualname__
    num_of_calls = redis.get(qualified_name).decode("utf-8")
    print("{} was called {} times:".format(qualified_name, num_of_calls))
    input_key = qualified_name + ":inputs"
    output_key = qualified_name + ":outputs"
    input_list = redis.lrange(input_key, 0, -1)
    output_list = redis.lrange(output_key, 0, -1)
    r_zipped = list(zip(input_list, output_list))
    for key, value in r_zipped:
        key = key.decode("utf-8")
        value = value.decode("utf-8")
        print("{}(*{}) -> {}".format(qualified_name, key, value))


class Cache:
    """Cache class."""

    def __init__(self):
        """Instantiate a redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store `data` in Redis using a random key and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """Get the value from Redis."""
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Parametise Cache.get to str."""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Parametise Cache.get to int."""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
