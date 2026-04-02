# Contributing to swisstopo-mcp

Thank you for your interest in contributing! Here is how to get started.

## Development Environment

```bash
git clone https://github.com/schulamt-gh/swisstopo-mcp.git
cd swisstopo-mcp
pip install -e ".[dev]"
```

This installs the package in editable mode along with all development dependencies (pytest, pytest-asyncio, respx, ruff).

## Running Tests

The test suite is split into unit tests (fast, no network) and live tests (hit real Swisstopo APIs):

```bash
# Unit tests only — run these before every commit
pytest tests/ -m "not live" -v

# All tests including live API calls (requires internet access)
pytest tests/ -v
```

Live tests are marked with `@pytest.mark.live` and are skipped in CI automatically.

## Code Style

This project uses [ruff](https://docs.astral.sh/ruff/) for both linting and formatting with a line length of 100:

```bash
# Check for lint issues
ruff check src/ tests/

# Auto-fix safe issues
ruff check --fix src/ tests/

# Format code
ruff format src/ tests/
```

Please run `ruff check` before submitting a pull request. The CI pipeline will fail if linting errors are present.

## Project Structure

```
src/swisstopo_mcp/
    __init__.py        # Package version
    server.py          # MCP server wiring (tool registrations)
    api_client.py      # Shared HTTP client (httpx + error handling)
    geocoding.py       # swisstopo_geocode, swisstopo_reverse_geocode
    rest_api.py        # swisstopo_search_layers, identify, find, get_feature
    height.py          # swisstopo_get_height, swisstopo_elevation_profile
    stac.py            # swisstopo_search_geodata, swisstopo_get_collection
    wmts.py            # swisstopo_map_url
    oereb.py           # swisstopo_get_egrid, swisstopo_get_oereb_extract
tests/
    test_geocoding.py
    test_rest_api.py
    test_height.py
    test_stac.py
    test_wmts.py
    test_oereb.py
```

## Pull Request Process

1. Fork the repository and create a branch from `main` (e.g. `feature/my-new-tool`).
2. Make your changes, add or update tests as appropriate.
3. Run the unit tests and linter locally and ensure everything passes.
4. Open a pull request against `main` with a clear description of what was changed and why.
5. The CI pipeline must pass before a PR can be merged.

## Adding a New Tool

1. Implement the tool logic in the appropriate module under `src/swisstopo_mcp/` (or create a new module).
2. Register the tool in `server.py` using `@mcp.tool(...)`.
3. Add unit tests in `tests/` using `respx` to mock HTTP responses.
4. Update the tool table in `README.md` and `README.de.md`.
5. Add an entry to `CHANGELOG.md` under `[Unreleased]`.

## Reporting Issues

Please open a GitHub issue with a clear description of the problem, including:
- Python version and OS
- Steps to reproduce
- Expected vs. actual behaviour
- Any relevant error messages or tracebacks
