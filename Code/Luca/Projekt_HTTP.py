#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python HTTP Projekt – Minimalsystem (Selenium + Requests)
Commands:
  - python myproject.py title [--url URL]             (scrape HTML tag content; default: <title>)
  - python myproject.py get [--url URL] [--param k=v]...
  - python myproject.py post [--url URL] [--data k=v]...
  - python myproject.py list-cookies [--url URL] [--headless 0|1]
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Dict, List, Tuple, Optional

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By


DEFAULT_SCRAPE_URL = "https://example.com"
DEFAULT_GET_URL = "https://httpbin.org/get"
DEFAULT_POST_URL = "https://httpbin.org/post"
DEFAULT_COOKIE_URL = "https://httpbin.org/cookies/set?course=python"


def parse_kv_list(items: Optional[List[str]]) -> Dict[str, str]:
    """Parse repeated k=v inputs into a dict."""
    result: Dict[str, str] = {}
    if not items:
        return result
    for raw in items:
        if "=" not in raw:
            raise ValueError(f"Invalid pair '{raw}'. Use k=v.")
        k, v = raw.split("=", 1)
        k = k.strip()
        if not k:
            raise ValueError(f"Invalid key in '{raw}'.")
        result[k] = v
    return result


def pretty_print(obj) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def http_get(url: str, params: Dict[str, str]) -> None:
    r = requests.get(url, params=params, timeout=20)
    print(f"Status: {r.status_code}")
    print(f"Final URL: {r.url}")
    try:
        pretty_print(r.json())
    except Exception:
        print(r.text)


def http_post(url: str, data: Dict[str, str]) -> None:
    r = requests.post(url, data=data, timeout=20)
    print(f"Status: {r.status_code}")
    print(f"Final URL: {r.url}")
    try:
        pretty_print(r.json())
    except Exception:
        print(r.text)


def make_driver(headless: bool) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    if headless:
        # modern Chrome headless
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Selenium Manager should handle driver resolution automatically in many setups.
    return webdriver.Chrome(options=options)


def scrape_tag(tag: str, url: str, headless: bool) -> None:
    tag = tag.strip().lower()
    if not tag:
        raise ValueError("Tag must not be empty (e.g. title, h1, p).")

    driver = make_driver(headless=headless)
    try:
        driver.get(url)

        if tag == "title":
            # simplest: driver.title uses the document title
            print(driver.title)
            return

        el = driver.find_element(By.TAG_NAME, tag)
        # textContent is usually robust (includes hidden text sometimes)
        txt = el.get_attribute("textContent") or el.text
        print((txt or "").strip())
    finally:
        driver.quit()


def list_cookies(url: str, headless: bool) -> None:
    driver = make_driver(headless=headless)
    try:
        driver.get(url)
        cookies = driver.get_cookies()
        pretty_print(cookies)
    finally:
        driver.quit()


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="myproject.py",
        description="Python HTTP Projekt – Minimalsystem (Selenium + Requests)"
    )
    sub = p.add_subparsers(dest="cmd")

    # GET
    p_get = sub.add_parser("get", help="HTTP GET with variables (params)")
    p_get.add_argument("--url", default=DEFAULT_GET_URL)
    p_get.add_argument("--param", action="append", help="Query param as k=v (repeatable)")

    # POST
    p_post = sub.add_parser("post", help="HTTP POST with variables (form data)")
    p_post.add_argument("--url", default=DEFAULT_POST_URL)
    p_post.add_argument("--data", action="append", help="Form field as k=v (repeatable)")

    # Cookies
    p_ck = sub.add_parser("list-cookies", help="List cookies via Selenium")
    p_ck.add_argument("--url", default=DEFAULT_COOKIE_URL)
    p_ck.add_argument("--headless", type=int, default=1, choices=[0, 1])

    # Scrape (optional as explicit command too)
    p_scr = sub.add_parser("scrape", help="Scrape HTML tag content via Selenium")
    p_scr.add_argument("tag", help="HTML tag name, e.g. title, h1, p")
    p_scr.add_argument("--url", default=DEFAULT_SCRAPE_URL)
    p_scr.add_argument("--headless", type=int, default=1, choices=[0, 1])

    return p


def main(argv: List[str]) -> int:
    # To match the assignment example: `python myproject.py title`
    # If first arg isn't a known subcommand, treat it as tag-scrape.
    known_cmds = {"get", "post", "list-cookies", "scrape", "-h", "--help"}
    if len(argv) >= 2 and argv[1] not in known_cmds and not argv[1].startswith("-"):
        tag = argv[1]
        # allow optional --url and --headless after the tag
        temp = argparse.ArgumentParser(add_help=False)
        temp.add_argument("--url", default=DEFAULT_SCRAPE_URL)
        temp.add_argument("--headless", type=int, default=1, choices=[0, 1])
        ns, _ = temp.parse_known_args(argv[2:])
        scrape_tag(tag=tag, url=ns.url, headless=bool(ns.headless))
        return 0

    parser = build_parser()
    args = parser.parse_args(argv[1:])

    try:
        if args.cmd == "get":
            params = parse_kv_list(args.param)
            http_get(url=args.url, params=params)
            return 0

        if args.cmd == "post":
            data = parse_kv_list(args.data)
            http_post(url=args.url, data=data)
            return 0

        if args.cmd == "list-cookies":
            list_cookies(url=args.url, headless=bool(args.headless))
            return 0

        if args.cmd == "scrape":
            scrape_tag(tag=args.tag, url=args.url, headless=bool(args.headless))
            return 0

        parser.print_help()
        return 2

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))