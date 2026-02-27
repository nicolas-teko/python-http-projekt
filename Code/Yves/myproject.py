import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

# -----------------------------
# GET-Methode: Seite öffnen + Scraping
# -----------------------------

def handle_get(parameter=None):
    driver = webdriver.Edge()
    driver.get("https://wikipedia.org")

    if parameter is None:
        print("Seite wurde geöffnet")
        input("Drücke Enter zum Beenden...")
        driver.quit()
        return

    try:
        parameter = parameter.lower()
        if parameter == "titel":
            print("Titel: ", driver.title)
        elif parameter == "h1":
            element = driver.find_element(By.TAG_NAME, "h1")
            print("H1: ", element.text)
        elif parameter == "img":
            images = driver.find_elements(By.TAG_NAME, "img")
            if not images:
                print("Keine Bilder gefunden.")
            for img in images:
                print("Image: ", img.get_attribute("src"))
        else:
            print("Unbekannter Parameter!!!")

    except Exception as e:
        print("Fehler", e)

    input("Drücke Enter zum Beenden...")
    driver.quit()

# -----------------------------
# POST-Methode: Formular ausfüllen
# -----------------------------

def handle_post(subcommand=None):
    if subcommand is None:
        print("Bitte Subcommand angeben, (z.B. 'login')")
        return
    if subcommand.lower() != "login":
        print(f"Unbekannter Subcommand '{subcommand}' für post")
        return
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/login")

    try:
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        username_input.send_keys("tom.smith")
        password_input.send_keys("SuperSecretPassword!")
        print("Login-Daten wurden automatisch eingetragen.")
    except Exception as e:
        print("Fehler", e)

    input("Drücke Enter zum Beenden...")
    driver.quit()

# -----------------------------
# Cookies-Methode: Cookies abrufen
# -----------------------------

def handle_cookies(subcommand=None):
    if subcommand is None:
        print("Bitte Subcommand angeben, (z.B. 'list')")
        return

    if subcommand.lower() != "list":
        print("Unbekannter Cookie-Subcommand!!!")
        return
    driver = webdriver.Edge()
    driver.get("https://wikipedia.org")

    try:
        cookies = driver.get_cookies()
        for cookie in cookies:
            print(cookie["name"], cookie["value"])

    except Exception as e:
        print("Fehler", e)

    input("Drücke Enter zum Beenden...")
    driver.quit()

# -----------------------------
# Main: CLI
# -----------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bitte Befehl angeben (z.B. get, post, cookies)")
    else:
        command = sys.argv[1].lower()

    if command == "get":
        handle_get(sys.argv[2] if len(sys.argv) == 3 else None)
    elif command == "post":
        handle_post(sys.argv[2] if len(sys.argv) == 3 else None)
    elif command == "cookies":
        handle_cookies(sys.argv[2] if len(sys.argv) == 3 else None)
    else:
        print("Unbekannter Command!!!")

