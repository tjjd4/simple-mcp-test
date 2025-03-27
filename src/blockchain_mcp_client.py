from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from typing import Any, Dict
from mcp.types import (
    CallToolResult, 
    # TextResourceContents, 
    # BlobResourceContents, 
    ReadResourceResult, 
    TextContent,
    ImageContent
)

async def call_mcp_tool(tool_name: str, params: Dict[str, Any]) -> CallToolResult:
    """Call a tool on the MCP server"""
    server_params = StdioServerParameters(
        command="npx",  # Use python3 to run the server
        args=["-y", "@mcpdotdirect/evm-mcp-server"],
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
        args=["-y", "@mcpdotdirect/evm-mcp-server"],
        env=None  # Optional environment variables
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.read_resource(resource_path) # type: ignore
            return result


async def get_eth_balance(address: str) -> str:
    """Get ETH balance for an address"""
    result = await call_mcp_tool("getBalance", {"address": address})
    content = result.content[0]
    if isinstance(content, TextContent):
        return content.text
    elif isinstance(content, ImageContent):
        return content.data
    else:
        raise ValueError(f"Unsupported content type: {type(content)}")


async def resolve_ens(ens_name: str) -> str:
    """Resolve ENS name to address"""
    result = await call_mcp_tool("resolveENS", {"name": ens_name})
    content = result.content[0]
    if isinstance(content, TextContent):
        return content.text
    elif isinstance(content, ImageContent):
        return content.data
    else:
        raise ValueError(f"Unsupported content type: {type(content)}")

async def get_token_balance(token_address: str, wallet_address: str) -> str:
    """Get token balance for an address"""
    result = await call_mcp_tool("getTokenBalance", {
        "tokenAddress": token_address,
        "walletAddress": wallet_address
    })
    content = result.content[0]
    if isinstance(content, TextContent):
        return content.text
    elif isinstance(content, ImageContent):
        return content.data
    else:
        raise ValueError(f"Unsupported content type: {type(content)}")