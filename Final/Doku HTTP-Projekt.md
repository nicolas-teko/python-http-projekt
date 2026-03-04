# Python HTTP Projekt Doku

## Funktionen

Das Programm `myproject.py` ist ein einfaches Python-Tool, um grundlegende Funktionen des HTTP-Protokolls und der Selenium Browser API zu testen.

Folgende Funktionen sind implementiert:

1. Anzeige des Inhalts eines HTML-Tags (z. B. `<title>`)
2. Durchführung eines **GET Requests**
3. Durchführung eines **POST Requests**
4. Anzeige aller Cookies einer Webseite

---

# Command Übersicht

| Command | Beschreibung | Beispiel |
|---|---|---|
| `title` | Liest den Inhalt des `<title>` HTML-Tags einer Webseite aus | `python myproject.py title https://example.com` |
| `get` | Sendet einen HTTP GET Request und gibt den HTML-Inhalt zurück | `python myproject.py get https://example.com` |
| `post` | Sendet einen HTTP POST Request mit einem Formularfeld | `python myproject.py post https://httpbin.org/post name max` |
| `list-cookies` | Zeigt alle Cookies einer Webseite an (via Selenium Browser) | `python myproject.py list-cookies https://example.com` |

---

# Ablauf / Nutzung des Programms

## 1. Terminal öffnen

In das Verzeichnis wechseln, in dem sich das Script befindet:


cd <projektordner>


---

## 2. Programm starten

Das Programm wird über die Kommandozeile gestartet:


python myproject.py <command> <url>


Je nach Command wird eine andere Funktion ausgeführt.

---

# Funktionen des Programms

## 1. HTML-Tag auslesen (Scraping)

Mit diesem Befehl wird der Inhalt des `<title>` Tags einer Webseite angezeigt.


python myproject.py title <url>


Beispiel:


python myproject.py title https://example.com


Das Programm:

1. sendet einen HTTP GET Request
2. lädt den HTML-Code der Seite
3. sucht nach dem `<title>` Tag
4. gibt den Inhalt im Terminal aus

Beispielausgabe:


Example Domain


---

## 2. GET Request

Mit diesem Befehl kann eine Webseite über einen **HTTP GET Request** geladen werden.


python myproject.py get <url>


Beispiel:


python myproject.py get https://example.com


Das Programm:

1. sendet einen HTTP GET Request an die angegebene URL
2. empfängt die Antwort des Servers
3. gibt den gesamten HTML-Inhalt der Seite im Terminal aus

---

## 3. POST Request

Mit diesem Befehl kann ein **HTTP POST Request** an eine Webseite gesendet werden.


python myproject.py post <url> <key> <value>


Beispiel:


python myproject.py post https://httpbin.org/post
 name max


Das Programm:

1. erstellt ein Formularfeld (`key=value`)
2. sendet dieses als POST Request an den Server
3. zeigt die Serverantwort im Terminal an

POST Requests werden typischerweise für:

- Login-Formulare
- Datenübermittlung
- API Requests

verwendet.

---

## 4. Cookies anzeigen

Mit diesem Befehl werden die Cookies einer Webseite angezeigt.


python myproject.py list-cookies <url>


Beispiel:


python myproject.py list-cookies https://example.com


Das Programm:

1. startet einen Browser mit Selenium
2. lädt die angegebene Webseite
3. liest alle Cookies aus
4. zeigt Name und Wert der Cookies im Terminal an

Beispielausgabe:


sessionid = abc123
csrftoken = 89sd8f7


---

# Verwendete Technologien

Dieses Projekt nutzt folgende Technologien:

- Python
- HTTP Protokoll
- Requests Library
- Selenium WebDriver

---

# Ziel des Projekts

Dieses Projekt dient dazu:

- die Funktionsweise des HTTP Protokolls zu verstehen
- GET und POST Requests praktisch anzuwenden
- Cookies von Webseiten auszulesen
- einfache Web-Scraping Methoden umzusetzen
- den Umgang mit Selenium und Browserautomatisierung zu lernen

---

# Zusammenfassung

Das Programm stellt einen einfachen HTTP-Testclient dar.

Folgende Funktionen werden unterstützt:

- HTML-Tag auslesen
- GET Requests senden
- POST Requests senden
- Cookies auslesen

Damit lassen sich grundlegende Mechanismen der Webkommunikation praktisch nachvollziehen.
