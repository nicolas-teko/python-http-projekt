# Selenium Browser CLI in Python (GET / POST / Cookies)

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

### 2. Abhängigkeiten installieren (nur falls nötig)
```bash
pip install selenium
```

**Wichtig:** Der Code nutzt `webdriver.Edge()`.  
Du brauchst **Microsoft Edge** installiert, und Selenium muss den passenden Driver finden (meist automatisch).

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

---

# Dokumentation: Selenium Browser CLI (GET / POST / Cookies)

## 1. Überblick
Dieses Projekt ist ein kleines **CLI-Tool** mit **Selenium**, das einen **Microsoft Edge** Browser startet und drei Funktionen anbietet:

- **GET / Scraping**: Öffnet eine Webseite und liest optional Inhalte aus (Titel, H1, Bilder)
- **POST / Login**: Füllt ein Login-Formular automatisch aus und sendet es ab (Testseite)
- **Cookies**: Liest Cookies einer Webseite aus und gibt sie in der Konsole aus

Die Steuerung erfolgt vollständig über Terminal-Befehle.

---

## 2. Grundidee des Programms
Das Tool ist so aufgebaut, dass du einen Hauptbefehl angibst:

- `get`
- `post`
- `cookies`
- `--help`

Je nach Befehl gibt es **Parameter/Subcommands** (z. B. `titel`, `login`, `list`) und optional eine **URL**.

---

## 3. CLI-Aufbau und Argument-Logik

### Syntax
```bash
python myproject.py <command> [parameter] [url]
```

### Logik im Code
- Wenn das **2. Argument** mit `http` beginnt → wird es als **URL** interpretiert
- Sonst → wird es als **Parameter/Subcommand** interpretiert
- Optional kann eine URL als **3. Argument** folgen

Beispiele:
- `python myproject.py get https://wikipedia.org`  
  → 2. Argument ist URL → Seite wird geöffnet

- `python myproject.py get titel https://wikipedia.org`  
  → 2. Argument ist Parameter (`titel`), 3. ist URL

---

## 4. GET (Scraping)

### Aufgabe
- Startet Edge
- Öffnet eine Webseite
- Gibt je nach Parameter Informationen aus:
  - `titel` → Seitentitel (`driver.title`)
  - `h1` → erste Überschrift `<h1>`
  - `img` → alle Bild-URLs aus `<img src="...">`

### Typische Ausgaben
- „Seite wurde geöffnet“ (ohne Parameter)
- „Titel: …“
- „Überschrift: …“
- „Image: …“ (für jedes Bild)

---

## 5. POST (Login)

### Aufgabe
- Öffnet eine Login-Testseite
- Findet Felder:
  - `#username`
  - `#password`
- Trägt fixe Testdaten ein
- Klickt den Submit-Button (`button[type='submit']`)

### Hinweis zur Kompatibilität
Andere Login-Seiten funktionieren nur, wenn sie:
- dieselben IDs (`username`, `password`) haben
- einen Submit-Button wie im Code besitzen

---

## 6. COOKIES (list)

### Aufgabe
- Öffnet eine Webseite
- Liest Cookies mit `driver.get_cookies()` aus
- Gibt pro Cookie:
  - Name
  - Value
aus

---

## 7. Fehlerfälle (typisch)
- **Unbekannter Command** → `Unbekannter Command!!!`
- **Unbekannter Parameter/Subcommand** → entsprechende Fehlermeldung
- **Element nicht gefunden** (z. B. kein H1 / falsche Login-Seite) → `Fehler <Exception>`

---

## 8. Zusammenfassung
- Einfache Selenium-CLI für Browser-Automation
- GET: öffnen + Scraping
- POST: Test-Login automatisch ausfüllen
- COOKIES: Cookies anzeigen
- Beenden immer via Enter → danach wird der Browser sauber geschlossen
