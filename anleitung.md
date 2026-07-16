# Schritt-für-Schritt: Amazon-Affiliate-Zwischenseiten für Pinterest

## 1. Domain besorgen (falls noch nicht vorhanden)

- Registrar z.B. IONOS, Strato, Namecheap, INWX (~10€/Jahr für eine `.de`-Domain)
- Name unabhängig von Amazon wählen (keine Marken-/Amazon-Begriffe im Domainnamen, sonst Markenrechtsprobleme)

## 2. Hosting einrichten

Zwei Wege, je nach Budget:

**A) Klassisches Webhosting (empfohlen, wenn du eh schon Kleingewerbe/Impressum planst)**
- Strato, IONOS, All-Inkl — Paket mit FTP/SFTP-Zugang reicht, kein WordPress nötig
- Du bekommst Zugangsdaten (Host, Benutzername, Passwort) für FTP

**B) Kostenlos, technisch (passt zu deinem Homelab-Hintergrund)**
- GitHub Pages oder Netlify — reines HTML wird kostenlos gehostet
- Vorteil: du pusht die generierten Dateien einfach per Git
- Nachteil: eigene Domain muss trotzdem separat registriert und per DNS (CNAME) verbunden werden

## 3. Ordnerstruktur anlegen

Auf deinem Rechner (oder direkt im Git-Repo):

```
affiliate-seiten/
├── produkte.csv          <- deine Produktliste
├── template.html          <- die Vorlage (nicht direkt bearbeiten)
├── generate.py             <- das Script
└── output/                 <- hier landen die fertigen Seiten
```

## 4. Produktliste pflegen (`produkte.csv`)

Eine Zeile pro Produkt. Spalten:

| slug | amazon_link |
|---|---|
| kaffeemuehle-modell-x | https://amzn.to/xxxxx |
| fermentierglas-set | https://amzn.to/yyyyy |

`slug` wird der Dateiname (`kaffeemuehle-modell-x.html`) — nur Kleinbuchstaben, Bindestriche, keine Umlaute/Leerzeichen.

## 5. Script laufen lassen

```bash
python3 generate.py
```

Erzeugt für jede Zeile in `produkte.csv` eine fertige HTML-Datei im `output/`-Ordner.

## 6. Hochladen

- **FTP-Hosting:** Ordner `output/` per FileZilla oder im Hosting-Panel in dein Web-Root hochladen
- **GitHub Pages/Netlify:** `output/`-Inhalt committen und pushen, Deployment läuft automatisch

## 7. URL prüfen

Im Browser aufrufen: `deinedomain.de/kaffeemuehle-modell-x.html` — Button muss zum richtigen Amazon-Link führen.

## 8. Pin bei Pinterest erstellen

- Pin-Ziel-URL = **deine** Seite (`deinedomain.de/kaffeemuehle-modell-x.html`), **nicht** der Amazon-Link
- Bilddatei fürs Pin selbst separat vorbereiten (eigenes Foto, kein reines Amazon-Produktbild)
- Pin-Beschreibung: kurzer Text + Hinweis "Werbung" oder "#affiliate", wie besprochen

## 9. Rechtliches nicht vergessen

- Impressum + Datenschutzerklärung müssen auf der Domain erreichbar sein (zentral reicht, z.B. `deinedomain.de/impressum.html`)
- Bei Kleingewerbe/gewerblicher Tätigkeit: Gewerbeanmeldung prüfen, sobald das über ein Hobby hinausgeht

## 10. Neue Produkte ergänzen

Einfach neue Zeile in `produkte.csv`, Script erneut laufen lassen, neue Datei hochladen. Bereits hochgeladene Seiten bleiben unberührt.
