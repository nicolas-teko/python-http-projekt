from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl
from src.browser import make_driver

def add_query_params(url: str, params: dict) -> str:
    parts = urlparse(url)
    query = dict(parse_qsl(parts.query))
    query.update({k: str(v) for k, v in params.items()})
    return urlunparse((parts.scheme, parts.netloc, parts.path, parts.params, urlencode(query), parts.fragment))

def run(url: str, headful: bool = False) -> None:
    driver = make_driver(headful=headful)
    try:
        target = add_query_params(url, {"q": "selenium", "page": 2})
        driver.get(target)
        print("Final URL:", driver.current_url)
        print("Title:", driver.title)
    finally:
        driver.quit()