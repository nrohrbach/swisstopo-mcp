# swisstopo-mcp

MCP-Server für schweizerische Bundgeodaten (Swisstopo-APIs)

Gibt KI-Assistenten (Claude, etc.) Zugriff auf die offizielle schweizerische Geodateninfrastruktur — Karten, Höhenmodelle, Geocodierung, Katasterauszüge und herunterladbare Datensätze — über 13 Tools aus 6 API-Familien.

[![CI](https://github.com/malkreide/swisstopo-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/malkreide/swisstopo-mcp/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/swisstopo-mcp.svg)](https://pypi.org/project/swisstopo-mcp/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Lizenz: MIT](https://img.shields.io/badge/Lizenz-MIT-yellow.svg)](LICENSE)

---

## Funktionen

- **13 Tools** aus **6 API-Familien** (REST, Geocoding, Höhe, STAC, WMTS, ÖREB)
- Schweizerische Adressen geocodieren und Koordinaten rückwärts geocodieren
- Höhe über Meer abfragen und Höhenprofile berechnen
- Geodatensätze entdecken und herunterladen (Orthophotos, 3D-Gebäude, historische Karten)
- Kartenobjekte an Koordinaten über 500+ Swisstopo-Layer identifizieren
- Teilbare map.geo.admin.ch-Links generieren
- Grundstück-IDs (EGRID) nachschlagen und ÖREB-Katasterauszüge abrufen

---

## Schnellstart

### Installation

```bash
pip install swisstopo-mcp
```

### Claude Desktop Konfiguration

Fügen Sie Folgendes in Ihre Claude Desktop Konfigurationsdatei `claude_desktop_config.json` ein:

```json
{
  "mcpServers": {
    "swisstopo": {
      "command": "swisstopo-mcp",
      "env": {
        "SWISSTOPO_OEREB_CANTONS": "ZH"
      }
    }
  }
}
```

Unter macOS befindet sich die Konfigurationsdatei unter `~/Library/Application Support/Claude/claude_desktop_config.json`.
Unter Windows unter `%APPDATA%\Claude\claude_desktop_config.json`.

---

## Tool-Übersicht

| Tool | Titel | Beschreibung |
|------|-------|-------------|
| `swisstopo_geocode` | Adresse geocodieren | Schweizerische Adressen, Ortsnamen oder PLZ in Koordinaten umwandeln |
| `swisstopo_reverse_geocode` | Koordinaten zu Adresse | Nächstgelegene Adresse zu gegebenen Koordinaten finden |
| `swisstopo_search_layers` | Swisstopo Layer suchen | Swisstopo-Layerkatalog (500+ Layer) nach Stichwort durchsuchen |
| `swisstopo_identify_features` | Features an Koordinate identifizieren | Kartenobjekte an einer bestimmten Koordinate finden (räumliche Abfrage) |
| `swisstopo_find_features` | Features nach Attribut suchen | Features anhand eines Attributwerts in einem Layer suchen (z.B. Gebäude nach EGID) |
| `swisstopo_get_feature` | Feature-Details abrufen | Vollständige Attribute und Geometrie eines Features per ID abrufen |
| `swisstopo_search_geodata` | Geodaten suchen | STAC-Katalog nach herunterladbaren Geodatensätzen durchsuchen |
| `swisstopo_get_collection` | Geodaten-Details abrufen | Details und Download-Links einer STAC-Collection abrufen |
| `swisstopo_map_url` | Karten-URL generieren | map.geo.admin.ch-URL zum Öffnen im Browser generieren |
| `swisstopo_get_height` | Höhe abfragen | Höhe über Meer (m ü. M.) an einer Koordinate abfragen |
| `swisstopo_elevation_profile` | Höhenprofil berechnen | Höhenprofil entlang einer Linie berechnen |
| `swisstopo_get_egrid` | Grundstück-ID (EGRID) ermitteln | Kataster-Grundstück-ID (EGRID) aus Koordinaten ermitteln |
| `swisstopo_get_oereb_extract` | ÖREB-Auszug abrufen | Öffentlich-rechtliche Eigentumsbeschränkungen (ÖREB) für ein Grundstück abrufen |

---

## Umgebungsvariablen

| Variable | Standard | Beschreibung |
|----------|---------|-------------|
| `SWISSTOPO_OEREB_CANTONS` | *(keiner)* | Kommagetrennte Liste der Kantone für ÖREB-Abfragen (z.B. `ZH,BE,LU`). Erforderlich für `swisstopo_get_egrid` und `swisstopo_get_oereb_extract`. |
| `MCP_TRANSPORT` | `stdio` | Transportprotokoll: `stdio` (Standard), `sse` oder `streamable-http` |
| `MCP_PORT` | `8000` | Port für SSE- oder HTTP-Transportmodus |

---

## Verwendungsbeispiele

### Adresse geocodieren

Fragen Sie Claude:
> "Wo befindet sich die Bahnhofstrasse 1, Zürich? Gib mir die Koordinaten."

Claude ruft `swisstopo_geocode` mit der Adresse auf und gibt WGS84-Koordinaten zurück.

### Höhe an einem Punkt abfragen

Fragen Sie Claude:
> "Welche Höhe hat der Uetliberg-Gipfel in Zürich?"

Claude geocodiert den Standort und ruft dann `swisstopo_get_height` auf.

### Features auf einem Kartenlayer identifizieren

Fragen Sie Claude:
> "Welche Gebäude befinden sich bei den Koordinaten 2683500, 1247500 (LV95)?"

Claude verwendet `swisstopo_identify_features` auf dem Gebäude-Layer.

### Grundstückseinschränkungen nachschlagen

Fragen Sie Claude:
> "Welche Nutzungseinschränkungen gelten für das Grundstück an der Musterstrasse 5, Zürich?"

Claude ruft `swisstopo_get_egrid` auf, um die EGRID zu ermitteln, und dann `swisstopo_get_oereb_extract` für den vollständigen Katasterauszug.

---

## Als HTTP-Server betreiben

Für Web-Anwendungen oder Multi-Client-Szenarien:

```bash
MCP_TRANSPORT=sse MCP_PORT=8080 swisstopo-mcp
```

---

## Entwicklung

### Einrichtung

```bash
git clone https://github.com/malkreide/swisstopo-mcp.git
cd swisstopo-mcp
pip install -e ".[dev]"
```

### Tests ausführen

```bash
# Nur Unit-Tests (kein Netzwerk erforderlich)
pytest tests/ -m "not live" -v

# Alle Tests inkl. Live-API-Aufrufe
pytest tests/ -v
```

### Code-Stil

Dieses Projekt verwendet [ruff](https://docs.astral.sh/ruff/) für Linting und Formatierung:

```bash
ruff check src/ tests/
ruff format src/ tests/
```

---

## Lizenz

MIT — siehe [LICENSE](LICENSE) für Details.

Daten bereitgestellt von [swisstopo](https://www.swisstopo.admin.ch/) unter den Bedingungen von [Open Government Data](https://opendata.swiss/).
