import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

# -----------------------------
# GET-Methode: Seite öffnen + Scraping
# -----------------------------

def handle_get(parameter=None, url=None):
    if url is None:
        url = "https://wikipedia.org"

    driver = webdriver.Chrome()
    driver.get(url)

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
            print("Überschrift: ", element.text)
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

def handle_post(subcommand=None, url=None):
    if subcommand is None:
        print("Bitte Subcommand angeben, (z.B. 'login')")
        return
    if subcommand.lower() != "login":
        print(f"Unbekannter Subcommand '{subcommand}' für post")
        return

    if url is None:
        url = "https://the-internet.herokuapp.com/login"

    driver = webdriver.Chrome()
    driver.get(url)

    try:
        # Eingabefeld finden
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        # Automatisch ausfüllen
        username_input.send_keys("tomsmith")
        password_input.send_keys("SuperSecretPassword!")

        # Login-Button klicken
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()


        print("Login-Daten wurden automatisch eingetragen.")
    except Exception as e:
        print("Fehler", e)

    input("Drücke Enter zum Beenden...")
    driver.quit()

# -----------------------------
# Cookies-Methode: Cookies abrufen
# -----------------------------

def handle_cookies(subcommand=None, url=None):

    # Standart URL
    if url is None:
        url = "https://wikipedia.org"

    # Wenn Subcommand fehlt
    if subcommand is None:
        print("Bitte Subcommand angeben, (z.B. 'list')")
        return

    # Wenn falscher Command
    if subcommand.lower() != "list":
        print("Unbekannter Cookie-Subcommand!!!")
        return

    driver = webdriver.Chrome()
    driver.get(url)

    try:
        cookies = driver.get_cookies()
        if not cookies:
            print("Keine Cookies gefunden.")
        for cookie in cookies:
            print(cookie["name"], cookie["value"])

    except Exception as e:
        print("Fehler", e)

    input("Drücke Enter zum Beenden...")
    driver.quit()

# -----------------------------
# Help Funktion zum anzeigen der Man Page
# -----------------------------
def handle_help():
    print("""
MyProject CLI - Übersicht der Befehle

Verwendung:
    python myproject.py <command> [parameter] [url]

Befehle:
    get [titel|h1|img] [url]        Öffnet eine Seite und zeigt Titel, H1 oder alle Bilder
    post login [url]                Füllt Login-Daten automatisch ein (Testseite)
    cookies list [url]              Listet alle Cookies der angegebenen Seite
    --help                          Zeigt diese Hilfe an

Beispiele:
    python myproject.py get titel https://google.com
    python myproject.py post login
    python myproject.py cookies list https://wikipedia.org
""")



# -----------------------------
# Main: CLI
# -----------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bitte Befehl angeben (z.B. get, post, cookies)")
    else:
        command = sys.argv[1].lower()

        parameter = None
        url = None

        # Prüfen ob parameter mit URL oder nur URL
        if len(sys.argv) >=3:
            if sys.argv[2].startswith("http"):
                url = sys.argv[2]
            else:
                parameter = sys.argv[2]

        # Viertes Argument prüfen parameter + URL
        if len(sys.argv) >= 4:
            url = sys.argv[3]

        # Funktionen Aufrufen
        if command == "get":
            handle_get(parameter, url)
        elif command == "post":
            handle_post(parameter, url)
        elif command == "cookies":
            handle_cookies(parameter, url)
        elif command == "--help":
            handle_help()
        else:
            print("Unbekannter Command!!!")

