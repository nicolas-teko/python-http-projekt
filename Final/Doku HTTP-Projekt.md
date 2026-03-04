# Selenium Browser CLI in Python (GET / POST / Cookies) NicolasW, Yves, Christian und Luca

## Funktionen
1. **GET** öffnet eine Webseite im Microsoft Edge Browser  
   - optional wird **Titel**, **H1** oder **alle Bild-URLs** ausgelesen
2. **POST (login)** öffnet eine Test-Loginseite und füllt Benutzername/Passwort automatisch aus
3. **COOKIES (list)** öffnet eine Webseite und listet alle Cookies (Name + Value) auf

---

## Ablauf

### 1. Terminal öffnen (1 Session)
Wechsle im Terminal in den Ordner, in dem deine Datei liegt (z. B. `myproject.py`).

Beispiel:
```bash
cd C:\Users\DEINNAME\Desktop\meinprojekt
```

---

### 2. Abhängigkeiten installieren (nur falls noch nicht Vorhanden)
```bash
pip install selenium
```

**Wichtig:** Der Code nutzt `webdriver.Edge()`.  
 **Microsoft Edge** installieren wenn nicht vorhanden, und Selenium muss den passenden Driver finden (meist automatisch).

---

### 3. Programm starten (Befehle kopierbar)

#### Hilfe anzeigen
```bash
python myproject.py --help
```

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

---

## POST: Login automatisch ausfüllen

### POST: Login ausführen (Default Testseite)
```bash
python myproject.py post login
```

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
