import anthropic
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

def create_server():
    mcp = FastMCP("POC MCP Server")

    @mcp.tool
    def ask_llm(prompt: str) -> str:
        """Pass a prompt to Claude and return the response."""
        client = anthropic.Anthropic()
        with client.messages.stream(
            model="claude-opus-4-6",
            max_tokens=16000,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            return stream.get_final_message().content[0].text

    @mcp.tool
    def greet_user(name: str) -> str:
        """Greet a user by name."""
        return f"Hello, {name}! Welcome to the POC MCP Server."

    return mcp


mcp = create_server()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8081))
    mcp.run(transport="http", host="0.0.0.0", port=port)