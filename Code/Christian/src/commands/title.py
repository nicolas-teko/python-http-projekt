from src.browser import make_driver

def run(url: str, headful: bool = False) -> None:
    driver = make_driver(headful=headful)
    try:
        driver.get(url)
        print(driver.title)
    finally:
        driver.quit()