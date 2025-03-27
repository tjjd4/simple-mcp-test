from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from typing import Any, Dict
from mcp.types import (
    CallToolResult, 
    TextResourceContents, 
    BlobResourceContents, 
    ReadResourceResult, 
    TextContent,
    ImageContent
)

async def call_mcp_tool(tool_name: str, params: Dict[str, Any]) -> CallToolResult:
    print("Starting EVM MCP Server...")
    """Call a tool on the MCP server"""
    server_params = StdioServerParameters(
        command="npx",  # Use python3 to run the server
        args=["-y", "@mcpdotdirect/evm-mcp-server"],
        env=None  # Optional environment variables
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            print("EVM MCP Server initialized")
            result = await session.call_tool(tool_name, params)
            return result

async def read_mcp_resource(resource_path: str) -> ReadResourceResult:
    """Read a resource from the MCP server"""
    server_params = StdioServerParameters(
        command="npx",  # Use python3 to run the server
        args=["-y", "@mcpdotdirect/evm-mcp-server"],
        env=None  # Optional environment variables
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.read_resource(resource_path) # type: ignore
            return result


async def get_eth_balance(address: str, network: str="ethereum") -> str:
    """Get ETH balance for an address"""
    result = await call_mcp_tool("get-balance", {"address": address, "network": network})
    print("Result:", result)
    content = result.content[0]
    if isinstance(content, TextContent):
        return content.text
    elif isinstance(content, ImageContent):
        return content.data
    else:
        raise ValueError(f"Unsupported content type: {type(content)}")


async def resolve_ens(ens_name: str, network: str="ethereum") -> str:
    """Resolve ENS name to address"""
    result = await call_mcp_tool("resolve-ens", {"ensName": ens_name, "network": network})
    content = result.content[0]
    if isinstance(content, TextContent):
        return content.text
    elif isinstance(content, ImageContent):
        return content.data
    else:
        raise ValueError(f"Unsupported content type: {type(content)}")

async def get_token_balance(token_address: str, owner_address: str, network: str="ethereum") -> str:
    """Get token balance for an address"""
    result = await call_mcp_tool("get-token-balance", {
        "tokenAddress": token_address,
        "ownerAddress": owner_address,
        "network": network
    })
    content = result.content[0]
    if isinstance(content, TextContent):
        return content.text
    elif isinstance(content, ImageContent):
        return content.data
    else:
        raise ValueError(f"Unsupported content type: {type(content)}")


async def read_chain_info(network: str="") -> str:
    if network == "":
        url = "evm://chain"
    else:
        url = f"evm://{network}/chain"
    result = await read_mcp_resource(url)
    content = result.contents[0]
    if isinstance(content, TextResourceContents):
        return content.text
    else:
        return content.blob
    

async def read_token_balance(token_address: str, address: str, network: str="ethereum") -> str:
    result = await read_mcp_resource(f"evm://{network}/token/{token_address}/balanceOf/{address}")
    content = result.contents[0]
    if isinstance(content, BlobResourceContents):
        return content.blob
    else:
        return content.text
        