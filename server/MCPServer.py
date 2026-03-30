from fastmcp import FastMCP

def create_server():
    mcp = FastMCP("POC MCP Server")

    @mcp.tool
    def greet(name: str) -> str:
        """Return a greeting."""
        return f"Hello, {name}!"

    return mcp

mcp = create_server()

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8081)
