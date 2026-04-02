# swisstopo-mcp

MCP server for Swiss federal geodata (Swisstopo APIs)

Gives AI assistants (Claude, etc.) access to Switzerland's official geodata infrastructure — maps, elevation, geocoding, cadastral extracts, and downloadable datasets — through 13 tools across 6 API families.

[![CI](https://github.com/schulamt-zh/swisstopo-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/schulamt-zh/swisstopo-mcp/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/swisstopo-mcp.svg)](https://pypi.org/project/swisstopo-mcp/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Features

- **13 tools** across **6 API families** (REST, Geocoding, Height, STAC, WMTS, ÖREB)
- Geocode Swiss addresses and reverse-geocode coordinates
- Query elevation and compute elevation profiles
- Discover and download geodatasets (orthophotos, 3D buildings, historical maps)
- Identify map features at coordinates across 500+ Swisstopo layers
- Generate shareable map.geo.admin.ch links
- Look up cadastral property IDs (EGRID) and retrieve ÖREB land-use restriction extracts

---

## Quick Start

### Installation

```bash
pip install swisstopo-mcp
```

### Claude Desktop Configuration

Add the following to your Claude Desktop `claude_desktop_config.json`:

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

On macOS the config file is at `~/Library/Application Support/Claude/claude_desktop_config.json`.
On Windows it is at `%APPDATA%\Claude\claude_desktop_config.json`.

---

## Tool Overview

| Tool | Title (DE) | Description |
|------|-----------|-------------|
| `swisstopo_geocode` | Adresse geocodieren | Convert Swiss addresses, place names, or postal codes to coordinates |
| `swisstopo_reverse_geocode` | Koordinaten zu Adresse | Find the nearest address for given coordinates |
| `swisstopo_search_layers` | Swisstopo Layer suchen | Search the Swisstopo layer catalog (500+ layers) by keyword |
| `swisstopo_identify_features` | Features an Koordinate identifizieren | Find map features at a specific coordinate (spatial query) |
| `swisstopo_find_features` | Features nach Attribut suchen | Search features by attribute value within a layer (e.g., buildings by EGID) |
| `swisstopo_get_feature` | Feature-Details abrufen | Retrieve full attributes and geometry for a feature by ID |
| `swisstopo_search_geodata` | Geodaten suchen | Search the STAC catalog for downloadable geodatasets |
| `swisstopo_get_collection` | Geodaten-Details abrufen | Get details and download links for a STAC collection |
| `swisstopo_map_url` | Karten-URL generieren | Generate a map.geo.admin.ch URL for browser display |
| `swisstopo_get_height` | Höhe abfragen | Get elevation above sea level (m a.s.l.) at a coordinate |
| `swisstopo_elevation_profile` | Höhenprofil berechnen | Compute an elevation profile along a line |
| `swisstopo_get_egrid` | Grundstück-ID (EGRID) ermitteln | Resolve a cadastral property ID (EGRID) from coordinates |
| `swisstopo_get_oereb_extract` | ÖREB-Auszug abrufen | Retrieve public-law land-use restrictions (ÖREB) for a parcel |

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SWISSTOPO_OEREB_CANTONS` | *(none)* | Comma-separated list of cantons to use for ÖREB queries (e.g. `ZH,BE,LU`). Required for `swisstopo_get_egrid` and `swisstopo_get_oereb_extract`. |
| `MCP_TRANSPORT` | `stdio` | Transport protocol: `stdio` (default), `sse`, or `streamable-http` |
| `MCP_PORT` | `8000` | Port for SSE or HTTP transport modes |

---

## Usage Examples

### Geocode an address

Ask Claude:
> "Where is Bahnhofstrasse 1, Zürich? Give me the coordinates."

Claude will call `swisstopo_geocode` with the address and return WGS84 coordinates.

### Get elevation at a point

Ask Claude:
> "What is the elevation at the Uetliberg summit in Zurich?"

Claude will geocode the location and then call `swisstopo_get_height`.

### Identify features on a map layer

Ask Claude:
> "What buildings are at coordinates 2683500, 1247500 (LV95)?"

Claude will use `swisstopo_identify_features` on the buildings layer.

### Look up property restrictions

Ask Claude:
> "What land-use restrictions apply to the parcel at Musterstrasse 5, Zürich?"

Claude will call `swisstopo_get_egrid` to find the EGRID, then `swisstopo_get_oereb_extract` for the full cadastral extract.

---

## Running as HTTP Server

For use in web applications or multi-client scenarios:

```bash
MCP_TRANSPORT=sse MCP_PORT=8080 swisstopo-mcp
```

---

## Development

### Setup

```bash
git clone https://github.com/schulamt-zh/swisstopo-mcp.git
cd swisstopo-mcp
pip install -e ".[dev]"
```

### Running Tests

```bash
# Unit tests only (no network required)
pytest tests/ -m "not live" -v

# All tests including live API calls
pytest tests/ -v
```

### Code Style

This project uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting:

```bash
ruff check src/ tests/
ruff format src/ tests/
```

---

## License

MIT — see [LICENSE](LICENSE) for details.

Data provided by [swisstopo](https://www.swisstopo.admin.ch/) under the [Open Government Data](https://opendata.swiss/) terms.
