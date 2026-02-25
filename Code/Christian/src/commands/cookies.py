from src.browser import make_driver

def run(url: str, headful: bool = False) -> None:
    driver = make_driver(headful=headful)
    try:
        driver.get(url)
        cookies = driver.get_cookies()
        if not cookies:
            print("(no cookies)")
            return
        for c in cookies:
            print(f"{c.get('name')}={c.get('value')}  domain={c.get('domain')} path={c.get('path')}")
    finally:
        driver.quit()