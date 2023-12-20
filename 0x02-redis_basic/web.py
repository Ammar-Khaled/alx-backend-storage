#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import requests
import redis

r = redis.Redis()


def get_page(url: str) -> str:
    """Use the requests module to obtain the HTML content of
    a particular URL and returns it."""
    r.incr(f"count:{url}")
    cached_html = r.get(f'cached:{url}')
    if cached_html:
        return cached_html.decode('utf-8')
    response = requests.get(url)
    r.setex(f'cached:{url}', 10, response.text)
    return response.text
