#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import requests
import redis
from typing import Callable
from functools import wraps

r = redis.Redis()


def track_requests(method: Callable) -> Callable:
    """Decorator."""
    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator functionality """
        r.incr(f"count:{url}")
        cached_html = r.get(f'cached:{url}')
        if cached_html:
            return cached_html.decode('utf-8')

        response = method(url)
        r.setex(f"cached:{url}", 10, response)
        return response

    return wrapper


def get_page(url: str) -> str:
    """Use the requests module to obtain the HTML content of
    a particular URL and returns it."""
    response = requests.get(url)
    return response.text
