# src/swisstopo_mcp/server.py
from __future__ import annotations

import os

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "swisstopo_mcp",
    instructions=(
        "Swiss federal geodata server with 13 tools across 6 API families. "
        "Use swisstopo_search_layers to discover layer IDs, then use "
        "swisstopo_identify_features or swisstopo_find_features to query them. "
        "swisstopo_geocode converts addresses to coordinates. "
        "swisstopo_get_height returns elevation. "
        "swisstopo_search_geodata finds downloadable datasets (orthophotos, 3D models, etc.). "
        "swisstopo_map_url generates shareable map links. "
        "ÖREB tools (swisstopo_get_egrid, swisstopo_get_oereb_extract) require a canton parameter."
    ),
)

# Tool imports will be added here as modules are implemented


def main():
    transport = os.environ.get("MCP_TRANSPORT", "stdio").lower()
    if transport in ("sse", "streamable-http"):
        port = int(os.environ.get("MCP_PORT", "8000"))
        mcp.run(transport=transport, port=port)
    else:
        mcp.run()


if __name__ == "__main__":
    main()
