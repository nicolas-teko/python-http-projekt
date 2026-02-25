from src.browser import make_driver
from selenium.webdriver.common.by import By

def run(url: str, headful: bool = False) -> None:
    driver = make_driver(headful=headful)
    try:
        driver.get(url)
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        print("Final URL:", driver.current_url)
        print("Result:", driver.find_element(By.ID, "flash").text.strip())
    finally:
        driver.quit()