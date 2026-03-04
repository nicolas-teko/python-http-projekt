#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python HTTP Projekt – Minimalsystem (Selenium + Requests)

Commands:
  - python <script>.py title [--url URL] [--headless 0|1] [--wait SEC] [--screenshot PATH]
  - python <script>.py get  [--url URL] [--param k=v]... [--timeout SEC] [--fail] [--out PATH]
  - python <script>.py post [--url URL] [--data  k=v]... [--timeout SEC] [--fail] [--out PATH]
  - python <script>.py list-cookies [--url URL] [--headless 0|1] [--wait SEC] [--screenshot PATH] [--out PATH]
  - python <script>.py scrape <tag> [--url URL] [--headless 0|1] [--wait SEC] [--screenshot PATH]

Shortcut:
  - python <script>.py title --url https://example.com
    (wenn das 1. Argument kein Subcommand ist, wird es als HTML-Tag interpretiert)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Dict, List, Optional, Any

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


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
            raise ValueError(f"Ungültiges Paar '{raw}'. Format: k=v")
        k, v = raw.split("=", 1)
        k = k.strip()
        if not k:
            raise ValueError(f"Ungültiger Key in '{raw}'.")
        result[k] = v
    return result


def pretty_print(obj: Any) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def save_json(path: Optional[str], obj: Any) -> None:
    if not path:
        return
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def http_get(url: str, params: Dict[str, str], timeout: float, fail: bool) -> Dict[str, Any]:
    r = requests.get(url, params=params, timeout=timeout)
    if fail:
        r.raise_for_status()
    result: Dict[str, Any] = {"status": r.status_code, "final_url": r.url}
    try:
        result["json"] = r.json()
    except Exception:
        result["text"] = r.text
    return result


def http_post(url: str, data: Dict[str, str], timeout: float, fail: bool) -> Dict[str, Any]:
    r = requests.post(url, data=data, timeout=timeout)
    if fail:
        r.raise_for_status()
    result: Dict[str, Any] = {"status": r.status_code, "final_url": r.url}
    try:
        result["json"] = r.json()
    except Exception:
        result["text"] = r.text
    return result


def make_driver(headless: bool) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def maybe_wait_for_title(driver: webdriver.Chrome, wait_sec: float) -> None:
    if wait_sec <= 0:
        return
    WebDriverWait(driver, wait_sec).until(lambda d: (d.title or "").strip() != "")


def maybe_wait_for_tag(driver: webdriver.Chrome, tag: str, wait_sec: float) -> None:
    if wait_sec <= 0:
        return
    WebDriverWait(driver, wait_sec).until(lambda d: len(d.find_elements(By.TAG_NAME, tag)) > 0)


def maybe_wait_for_any_cookie(driver: webdriver.Chrome, wait_sec: float) -> None:
    if wait_sec <= 0:
        return
    try:
        WebDriverWait(driver, wait_sec).until(lambda d: len(d.get_cookies()) > 0)
    except Exception:
        # Manche Seiten setzen bewusst keine Cookies -> nicht hart abbrechen
        pass


def scrape_tag(tag: str, url: str, headless: bool, wait_sec: float, screenshot: Optional[str]) -> None:
    tag = tag.strip().lower()
    if not tag:
        raise ValueError("Tag darf nicht leer sein (z.B. title, h1, p).")

    driver = make_driver(headless=headless)
    try:
        driver.get(url)

        if tag == "title":
            maybe_wait_for_title(driver, wait_sec)
            if screenshot:
                driver.save_screenshot(screenshot)
            print(driver.title)
            return

        maybe_wait_for_tag(driver, tag, wait_sec)
        if screenshot:
            driver.save_screenshot(screenshot)

        el = driver.find_element(By.TAG_NAME, tag)
        txt = el.get_attribute("textContent") or el.text
        print((txt or "").strip())
    finally:
        driver.quit()


def list_cookies(url: str, headless: bool, wait_sec: float, screenshot: Optional[str], out: Optional[str]) -> None:
    driver = make_driver(headless=headless)
    try:
        driver.get(url)
        maybe_wait_for_any_cookie(driver, wait_sec)

        if screenshot:
            driver.save_screenshot(screenshot)

        cookies = driver.get_cookies()

        # Für die Aufgabenanforderung: "Liste aller Cookies ausgeben"
        pretty_print(cookies)

        # Optional in Datei speichern (mit URL als Kontext)
        save_json(out, {"url": url, "cookies": cookies})
    finally:
        driver.quit()


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        description="Python HTTP Projekt – Minimalsystem (Selenium + Requests)",
    )
    sub = p.add_subparsers(dest="cmd")

    # GET
    p_get = sub.add_parser("get", help="HTTP GET mit Variablen (params)")
    p_get.add_argument("--url", default=DEFAULT_GET_URL)
    p_get.add_argument("--param", action="append", help="Query-Parameter als k=v (mehrfach möglich)")
    p_get.add_argument("--timeout", type=float, default=20.0, help="Timeout in Sekunden")
    p_get.add_argument("--fail", action="store_true", help="Bei HTTP 4xx/5xx als Fehler abbrechen")
    p_get.add_argument("--out", help="Ergebnis zusätzlich als JSON-Datei speichern")

    # POST
    p_post = sub.add_parser("post", help="HTTP POST mit Variablen (Form-Daten)")
    p_post.add_argument("--url", default=DEFAULT_POST_URL)
    p_post.add_argument("--data", action="append", help="Form-Feld als k=v (mehrfach möglich)")
    p_post.add_argument("--timeout", type=float, default=20.0, help="Timeout in Sekunden")
    p_post.add_argument("--fail", action="store_true", help="Bei HTTP 4xx/5xx als Fehler abbrechen")
    p_post.add_argument("--out", help="Ergebnis zusätzlich als JSON-Datei speichern")

    # Cookies
    p_ck = sub.add_parser("list-cookies", help="Cookies via Selenium anzeigen")
    p_ck.add_argument("--url", default=DEFAULT_COOKIE_URL)
    p_ck.add_argument("--headless", type=int, default=1, choices=[0, 1])
    p_ck.add_argument("--wait", type=float, default=0.0, help="Explizit warten (Sekunden), bis Cookies da sind")
    p_ck.add_argument("--screenshot", help="Screenshot speichern (Pfad)")
    p_ck.add_argument("--out", help="Ergebnis zusätzlich als JSON-Datei speichern")

    # Scrape
    p_scr = sub.add_parser("scrape", help="HTML-Tag-Inhalt via Selenium auslesen")
    p_scr.add_argument("tag", help="HTML Tag, z.B. title, h1, p")
    p_scr.add_argument("--url", default=DEFAULT_SCRAPE_URL)
    p_scr.add_argument("--headless", type=int, default=1, choices=[0, 1])
    p_scr.add_argument("--wait", type=float, default=0.0, help="Explizit warten (Sekunden), bis Inhalt da ist")
    p_scr.add_argument("--screenshot", help="Screenshot speichern (Pfad)")

    return p


def main(argv: List[str]) -> int:
    # Shortcut: `python <script>.py title` soll funktionieren (Tag direkt).
    known_cmds = {"get", "post", "list-cookies", "scrape", "-h", "--help"}
    if len(argv) >= 2 and argv[1] not in known_cmds and not argv[1].startswith("-"):
        tag = argv[1]
        temp = argparse.ArgumentParser(add_help=False)
        temp.add_argument("--url", default=DEFAULT_SCRAPE_URL)
        temp.add_argument("--headless", type=int, default=1, choices=[0, 1])
        temp.add_argument("--wait", type=float, default=0.0)
        temp.add_argument("--screenshot")
        ns, _ = temp.parse_known_args(argv[2:])
        scrape_tag(
            tag=tag,
            url=ns.url,
            headless=bool(ns.headless),
            wait_sec=float(ns.wait),
            screenshot=ns.screenshot,
        )
        return 0

    parser = build_parser()

    # Ohne Argumente: Hilfe anzeigen und sauber beenden
    if len(argv) == 1:
        parser.print_help()
        return 0

    args = parser.parse_args(argv[1:])

    try:
        if args.cmd == "get":
            params = parse_kv_list(args.param)
            result = http_get(
                url=args.url,
                params=params,
                timeout=float(args.timeout),
                fail=bool(args.fail),
            )
            print(f"Status: {result['status']}")
            print(f"Final URL: {result['final_url']}")
            if "json" in result:
                pretty_print(result["json"])
            else:
                print(result.get("text", ""))
            save_json(args.out, result)
            return 0

        if args.cmd == "post":
            data = parse_kv_list(args.data)
            result = http_post(
                url=args.url,
                data=data,
                timeout=float(args.timeout),
                fail=bool(args.fail),
            )
            print(f"Status: {result['status']}")
            print(f"Final URL: {result['final_url']}")
            if "json" in result:
                pretty_print(result["json"])
            else:
                print(result.get("text", ""))
            save_json(args.out, result)
            return 0

        if args.cmd == "list-cookies":
            list_cookies(
                url=args.url,
                headless=bool(args.headless),
                wait_sec=float(args.wait),
                screenshot=args.screenshot,
                out=args.out,
            )
            return 0

        if args.cmd == "scrape":
            scrape_tag(
                tag=args.tag,
                url=args.url,
                headless=bool(args.headless),
                wait_sec=float(args.wait),
                screenshot=args.screenshot,
            )
            return 0

        parser.print_help()
        return 0

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))