from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from typing import Any, Dict, Optional
from mcp.types import (
    CallToolResult, 
    TextResourceContents, 
    BlobResourceContents, 
    ReadResourceResult, 
    TextContent,
    ImageContent
)

async def call_mcp_tool(tool_name: str, params: Dict[str, Any]) -> CallToolResult:
    """Call a tool on the MCP server"""
    server_params = StdioServerParameters(
        command="python3",  # Use python3 to run the server
        args=["src/simple_mcp_server.py"],  # Path to server.py
        env=None  # Optional environment variables
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, params)
            return result

async def read_mcp_resource(resource_path: str) -> ReadResourceResult:
    """Read a resource from the MCP server"""
    server_params = StdioServerParameters(
        command="python3",  # Use python3 to run the server
        args=["src/simple_mcp_server.py"],  # Path to server.py
        env=None  # Optional environment variables
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.read_resource(resource_path) # type: ignore
            return result

async def add_numbers(a: int, b: int) -> Optional[str]:
    """Add two numbers using the server's add tool"""
    result = await call_mcp_tool("add", {"a": a, "b": b})
    content = result.content[0]
    if isinstance(content, TextContent):
        return content.text
    elif isinstance(content, ImageContent):
        return content.data
    else:
        raise ValueError(f"Unsupported content type: {type(content)}")

async def get_greeting(name: str) -> Optional[str]:
    result = await read_mcp_resource(f"greeting://{name}")
    content = result.contents[0]
    # content is TextResourceContents or BlobResourceContents
    if isinstance(content, TextResourceContents):
        return content.text
    else:
        return content.blob

async def get_current_time() -> Optional[str]:
    result = await read_mcp_resource("time://")
    content = result.contents[0]
    # content is TextResourceContents or BlobResourceContents
    if isinstance(content, BlobResourceContents):
        return content.blob
    else:
        return content.text