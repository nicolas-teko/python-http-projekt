# Selenium Browser CLI in Python (GET / POST / Cookies) NicolasW, Yves, Christian und Luca

## Funktionen
1. **GET** öffnet eine Webseite im Chrome Browser  
   - optional wird **Titel**, **H1** oder **alle Bild-URLs** ausgelesen
2. **POST (login)** öffnet eine Test-Loginseite und füllt Benutzername/Passwort automatisch aus
3. **COOKIES (list)** öffnet eine Webseite und listet alle Cookies (Name + Value) auf

**Wichtiges!**
1. Wenn man eine Webseite als Parameter angibt, muss man immer mit http:// oder https:// starten da der Parameter erst dann zum tragen kommt. (Bsp. python myproject.py get titel https://google.com)
---

## Ablauf

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
