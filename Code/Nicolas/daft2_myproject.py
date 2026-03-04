import sys                      # Zugriff auf Kommandozeilenargumente
import re                       # Für einfache HTML-Tag-Suche (ohne extra Libraries)
import requests                 # Für GET/POST Requests
from selenium import webdriver  # Selenium-Modul zum Steuern eines Browsers


def list_cookies(url):
    driver = webdriver.Chrome()        # Startet einen Chrome-Browser über Selenium
    driver.get(url)                    # Öffnet die angegebene URL im Browser

    cookies = driver.get_cookies()     # Liest alle Cookies der aktuell geladenen Seite aus
    for c in cookies:                  # Iteriert durch alle gefundenen Cookies
        print(f"{c['name']} = {c['value']}")  # Gibt Cookie-Name und Cookie-Wert aus

    driver.quit()                      # Schließt den Browser wieder


def print_title(url):
    r = requests.get(url, timeout=20)  # Führt einen GET Request aus
    r.raise_for_status()               # Bricht ab, wenn HTTP Fehler (z.B. 404)

    m = re.search(r"<title[^>]*>(.*?)</title>", r.text, flags=re.IGNORECASE | re.DOTALL)
    if m:
        title = re.sub(r"\s+", " ", m.group(1)).strip()  # Whitespace normalisieren
        print(title)                 # Titel ausgeben
    else:
        print("Kein <title> Tag gefunden.")  # Falls kein title Tag vorhanden ist


def do_get(url):
    r = requests.get(url, timeout=20)  # Einfacher GET Request ohne Variablen
    r.raise_for_status()               # Bricht ab, wenn HTTP Fehler
    print(r.text)                      # Antwort-Body ausgeben (simpel)


def do_post(url, key, value):
    data = {key: value}                # Erstellt ein Dictionary mit dem Formularfeld
    r = requests.post(url, data=data)  # Sendet POST Request mit diesen Daten
    r.raise_for_status()               # Stoppt bei HTTP Fehler
    print(r.text)                      # Antwort anzeigen


def usage():
    print("Mögliche Commands:")
    print("  python myproject.py cookies list <url>")
    print("  python myproject.py title <url>")
    print("  python myproject.py get <url>")
    print("  python myproject.py post <url> <key> <value>")


def main():
    if len(sys.argv) < 3:              # Mindestanzahl Argumente prüfen
        usage()
        return

    command = sys.argv[1]              # Erstes Argument bestimmt die Aktion

    # cookies list <url>
    if command == "cookies":
        if len(sys.argv) == 4 and sys.argv[2] == "list":
            url = sys.argv[3]          # URL ist das dritte Argument (nach cookies list)
            list_cookies(url)          # Cookies auslesen und ausgeben
        else:
            usage()                    # Falsche Eingabe -> Hilfe anzeigen
        return

    # title <url>
    if command == "title":
        if len(sys.argv) == 3:
            url = sys.argv[2]          # URL ist das zweite Argument (nach title)
            print_title(url)           # <title> auslesen und ausgeben
        else:
            usage()                    # Falsche Eingabe -> Hilfe anzeigen
        return

    # get <url>
    if command == "get":
        if len(sys.argv) == 3:
            url = sys.argv[2]          # URL ist das zweite Argument (nach get)
            do_get(url)                # GET Request ausführen
        else:
            usage()                    # Falsche Eingabe -> Hilfe anzeigen
        return

    # post <url>
    if command == "post":
        if len(sys.argv) == 5:
            url = sys.argv[2]  # Ziel-URL
            key = sys.argv[3]  # Name des Formularfeldes
            value = sys.argv[4]  # Wert des Formularfeldes
            do_post(url, key, value)  # POST Request ausführen
        else:
            usage()
        return                            # Unbekannter Command -> Hilfe anzeigen


if __name__ == "__main__":             # Stellt sicher, dass main nur beim direkten Start läuft
    main()