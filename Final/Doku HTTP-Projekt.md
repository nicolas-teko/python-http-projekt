# Python HTTP Projekt (GET / POST / Cookies) NicolasW, Yves, Christian und Luca

## Funktionen
1. **GET** öffnet eine Webseite im Chrome Browser  
   - optional wird **Titel**, **H1** oder **alle Bild-URLs** ausgelesen
2. **POST (login)** öffnet eine Test-Loginseite und füllt Benutzername/Passwort automatisch aus
3. **COOKIES (list)** öffnet eine Webseite und listet alle Cookies (Name + Value) auf

**Wichtiges!**
 - Wenn man eine Webseite als Parameter angibt, muss man immer mit http:// oder https:// starten da der Parameter erst dann zum tragen kommt. (Bsp. python myproject.py get titel https://google.com)

---

## Anleitung

### 1. Terminal öffnen (1 Session)
Wechsle im Terminal in den Ordner, in dem deine Datei liegt (z. B. `myproject.py`).

Beispiel:
```bash
cd C:\Users\DEINNAME\Desktop\meinprojekt

```
<img width="1304" height="235" alt="Konsole_move_to_project" src="https://github.com/user-attachments/assets/35f02f7c-9c56-4047-878b-108f8d543fcc" />

---

### 2. Abhängigkeiten installieren (nur falls noch nicht Vorhanden)
```bash
pip install selenium
```

**Wichtig:** Der Code nutzt `webdriver.Chrome()`.  
 **Google Chrome** installieren wenn nicht vorhanden, und Selenium muss den passenden Driver finden (meist automatisch).

---

### 3. Programm starten (Befehle kopierbar)

#### Hilfe anzeigen
```bash
python myproject.py --help
```
<img width="1205" height="592" alt="Konsole_help" src="https://github.com/user-attachments/assets/b5286ad4-2e51-44ba-ba8e-d38c11a7b496" />

---

## GET: Seite öffnen / Scraping

### GET: Seite nur öffnen (Default: Wikipedia)
```bash
python myproject.py get
```
→ Öffnet `https://wikipedia.org` und wartet auf Enter.

### GET: Titel auslesen
```bash
python myproject.py get titel https://wikipedia.org
```

### GET: H1 auslesen
```bash
python myproject.py get h1 https://wikipedia.org
```

### GET: Alle Bilder (img src) auslesen
```bash
python myproject.py get img https://wikipedia.org
```

**Hinweis:** Wenn du keine URL angibst, wird automatisch Wikipedia geöffnet:
```bash
python myproject.py get titel
```

<img width="1425" height="422" alt="Konsole_GET_title" src="https://github.com/user-attachments/assets/c0b70d56-7dd2-4117-b751-59df095af7ec" />

---

## POST: Login automatisch ausfüllen

### POST: Login ausführen (Default Testseite)
```bash
python myproject.py post login
```
<img width="1345" height="778" alt="Konsole_POST_Login" src="https://github.com/user-attachments/assets/1ef01e40-b162-4440-aae9-2d2e4654c569" />

Default URL:
- `https://the-internet.herokuapp.com/login`

Der Code trägt automatisch ein:
- Username: `tomsmith`
- Password: `SuperSecretPassword!`
und klickt danach auf **Login**.

**Optional mit URL (nur wenn die Seite gleiche Felder hat!)**
```bash
python myproject.py post login https://the-internet.herokuapp.com/login
```

---

## COOKIES: Cookies anzeigen

### COOKIES: Cookies anzeigen (Default: Wikipedia)
```bash
python myproject.py cookies list
```
<img width="1527" height="409" alt="Konsole_cookies_list" src="https://github.com/user-attachments/assets/1465838a-5499-41f3-abf6-55bdb0a69ede" />

### COOKIES: Cookies einer bestimmten Seite anzeigen
```bash
python myproject.py cookies list https://wikipedia.org
```

---

## Programm beenden
Am Ende wartet das Programm immer auf:

```text
Drücke Enter zum Beenden...
```

Erst danach wird der Browser geschlossen (`driver.quit()`).

## Verwendete Technologien und Konzepte

### Selenium
Selenium ist eine Bibliothek zur automatisierten Steuerung von Webbrowsern. Damit kann ein Programm Webseiten öffnen, auf Elemente klicken, Formulare ausfüllen oder Inhalte auslesen. So als würde ein Benutzer den Browser selbst bedienen. In diesem Projekt wird Selenium verwendet, um den Chrome-Browser automatisch zu starten, Webseiten zu laden und Informationen aus dem HTML der Seite auszulesen.
...

### HTTP
HTTP (Hypertext Transfer Protocol) ist das grundlegende Protokoll des Webs. Es definiert, wie ein Client (z. B. ein Browser) eine Anfrage an einen Webserver sendet und wie der Server darauf antwortet. Typische HTTP-Methoden sind wie oben GET zum Abrufen von Daten und POST zum Senden von Daten an einen Server, beispielsweise beim Login in ein Formular.
...

### Cookies
Cookies sind kleine Datensätze, die eine Webseite im Browser speichert. Sie enthalten meist Informationen über eine Sitzung, Einstellungen oder Benutzeridentifikation. Webserver können Cookies nutzen um Benutzer wiederzuerkennen oder Login-Sessions am laufen zu halten. In diesem Projekt werden Cookies einer Webseite ausgelesen und im Terminal mit ihrem Namen und Wert dann angezeigt.
...

### Web Scraping
Web Scraping bezeichnet das automatisierte Auslesen von Informationen aus Webseiten. Dabei wird der HTML-Inhalt einer Seite analysiert, um  Elemente wie Überschriften, Bilder oder Texte auszulesen. In diesem Projekt wird wie oben gennant Selenium verwendet, um Inhalte wie den Seitentitel, H1-Überschriften oder Bild-URLs aus einer geladenen Webseite zu sammeln.
...

### WebDriver
Der WebDriver ist hier die Schnittstelle zwischen Selenium und den Webbrowser. In diesem Projekt wird der Chrome WebDriver verwendet, der über webdriver.Chrome() gestartet wird und die Steuerung des Chrome-Browser übernimmt.
...

