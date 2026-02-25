from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def make_driver(headful: bool = False) -> webdriver.Chrome:
    options = Options()
    if not headful:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)