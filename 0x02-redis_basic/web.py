#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import requests
import redis
from typing import Callable
from functools import wraps

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Decorator for counting how many times a request
    has been made """

    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator functionality """
        r.incr(f"count:{url}")
        cached_html = r.get(f'cached:{url}')
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Uses the requests module to obtain the HTML
    content of a particular URL and returns it.
    """
    req = requests.get(url)
    return req.text


if __name__ == "__main__":
    import time
    before = time.perf_counter()
    print(get_page('http://slowwly.robertomurray.co.uk'))
    print(time.perf_counter() - before)
