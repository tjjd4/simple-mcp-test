from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.resource("time://")
def get_time() -> str:
    """Get the current time"""
    return datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    mcp.run()
