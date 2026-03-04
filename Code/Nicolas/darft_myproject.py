import sys                      # Zugriff auf Kommandozeilenargumente
import re                       # Für einfache HTML-Tag-Suche (ohne extra Libraries)
import requests                 # Für GET/POST Requests
from selenium import webdriver  # Selenium-Modul zum Steuern eines Browsers


def parse_kv_args(pairs):
    # Nimmt Argumente im Format key=value und macht daraus ein Dict
    data = {}
    for p in pairs:
        if "=" not in p:
            continue            # Ignoriert alles, was nicht key=value ist
        k, v = p.split("=", 1)  # Nur beim ersten '=' splitten (Werte dürfen '=' enthalten)
        data[k] = v
    return data


def list_cookies(url):
    driver = webdriver.Chrome()        # Startet einen Chrome-Browser über Selenium
    driver.get(url)                    # Öffnet die angegebene URL im Browser

    cookies = driver.get_cookies()     # Liest alle Cookies der aktuell geladenen Seite aus
    for c in cookies:                  # Iteriert durch alle gefundenen Cookies
        print(f"{c['name']} = {c['value']}")  # Gibt Cookie-Name und Cookie-Wert aus

    driver.quit()                      # Schließt den Browser wieder


def print_title(url):
    # Einfachstes Scraping: Seite laden und <title>...</title> aus dem HTML ziehen
    # (Achtung: wenn Titel erst per JS nachgeladen wird, kann requests das nicht sehen)
    r = requests.get(url, timeout=20)  # Führt einen GET Request aus
    r.raise_for_status()               # Bricht ab, wenn HTTP Fehler (z.B. 404)

    m = re.search(r"<title[^>]*>(.*?)</title>", r.text, flags=re.IGNORECASE | re.DOTALL)
    if m:
        title = re.sub(r"\s+", " ", m.group(1)).strip()  # Whitespace normalisieren
        print(title)
    else:
        print("Kein <title> Tag gefunden.")


def do_get(url, pairs):
    params = parse_kv_args(pairs)          # URL-Parameter aus key=value bauen
    r = requests.get(url, params=params, timeout=20)  # GET mit Query-Parametern
    r.raise_for_status()
    print(r.text)                          # Antwort-Body ausgeben (simpel)


def do_post(url, pairs):
    data = parse_kv_args(pairs)            # Form-Fields aus key=value bauen
    r = requests.post(url, data=data, timeout=20)      # POST als Form-Submission
    r.raise_for_status()
    print(r.text)                          # Antwort-Body ausgeben (simpel)


def usage():
    print("Mögliche Commands:")
    print("  python myproject.py cookies list <url>")
    print("  python myproject.py title <url>")
    print("  python myproject.py get <url> [key=value ...]")
    print("  python myproject.py post <url> [key=value ...]")


def main():
    if len(sys.argv) < 3:                  # Mindestanzahl Argumente prüfen
        usage()
        return

    command = sys.argv[1]                 # Erstes Argument bestimmt die Aktion

    # cookies list <url>
    if command == "cookies":
        if len(sys.argv) == 4 and sys.argv[2] == "list":
            url = sys.argv[3]
            list_cookies(url)
        else:
            usage()
        return

    # title <url>
    if command == "title":
        if len(sys.argv) == 3:
            url = sys.argv[2]
            print_title(url)
        else:
            usage()
        return

    # get <url> [key=value ...]
    if command == "get":
        url = sys.argv[2]
        pairs = sys.argv[3:]              # Alles nach der URL sind Variablen (optional)
        do_get(url, pairs)
        return

    # post <url> [key=value ...]
    if command == "post":
        url = sys.argv[2]
        pairs = sys.argv[3:]              # Alles nach der URL sind Variablen (optional)
        do_post(url, pairs)
        return

    usage()                                # Unbekannter Command


if __name__ == "__main__":                 # Stellt sicher, dass main nur beim direkten Start läuft
    main()