
from fastmcp.tools import tool
from fastmcp import FastMCP

mcp = FastMCP("POC MCP Server")
@tool
def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()

