import sys                     # Zugriff auf Kommandozeile
from selenium import webdriver # Selenium-Modul zum Steuern eines Browsers


def list_cookies(url):
    driver = webdriver.Chrome()     # Startet einen Chrome-Browser über Selenium
    driver.get(url)                 # Öffnet die angegebene URL im Browser

    cookies = driver.get_cookies()  # Liest alle Cookies der aktuell geladenen Seite auf

    for c in cookies:               # Iteriert durch alle gefundenen Cookies
        print(f"{c['name']} = {c['value']}")  # Gibt Cookie-Name und Cookie-Wert aus

    driver.quit()                   # Schließt den Browser wieder


def main():
    if len(sys.argv) == 4:          # Prüft ob genau 3 Argumente übergeben wurden
        command = sys.argv[1]       # Erstes Argument (z.B. "cookies")
        action = sys.argv[2]        # Zweites Argument (z.B. "list")
        url = sys.argv[3]           # Drittes Argument ist die Ziel-URL

        if command == "cookies" and action == "list":  # Prüft ob der richtige Befehl verwendet wurde
            list_cookies(url)       # Führt die Funktion zum Auslesen der Cookies aus
        else:
            print("Bitte: python script.py cookies list <url>")  # Fehlermeldung bei falschem Befehl
    else:
        print("Bitte: python script.py cookies list <url>")      # Hinweis wenn falsche Anzahl Argumente


if __name__ == "__main__":          # Stellt sicher, dass main nur beim direkten Start des Skripts ausgeführt wird
    main()