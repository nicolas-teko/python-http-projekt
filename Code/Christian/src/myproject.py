import argparse

from src.commands.title import run as run_title
from src.commands.get import run as run_get
from src.commands.post import run as run_post
from src.commands.cookies import run as run_cookies

DEFAULT_URL = "https://example.com"

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="myproject")
    parser.add_argument("--url", default=DEFAULT_URL, help="Target URL")
    parser.add_argument("--headful", action="store_true", help="Show browser window (not headless)")

    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("title", help="Print page title")
    sub.add_parser("get", help="GET with variables (query params)")
    sub.add_parser("post", help="POST form submission")
    sub.add_parser("list-cookies", help="List cookies")

    return parser

def main() -> None:
    args = build_parser().parse_args()

    if args.command == "title":
        run_title(url=args.url, headful=args.headful)
    elif args.command == "get":
        run_get(url=args.url, headful=args.headful)
    elif args.command == "post":
        run_post(url=args.url, headful=args.headful)
    elif args.command == "list-cookies":
        run_cookies(url=args.url, headful=args.headful)

if __name__ == "__main__":
    main()