#!/usr/bin/env python3
import asyncio
from src.blockchain_mcp_client import get_eth_balance, resolve_ens, get_token_balance, read_chain_info, read_token_balance

async def main():
    """Example usage of the blockchain MCP client"""
    print("Testing blockchain MCP client...")


    
    # Test ETH balance
    print("\nTesting ETH balance...")
    eth_address = "0x860201656ece07cb8d5133dd704bb6f10a09fe93"  # Example address
    balance = await get_eth_balance(eth_address, network="ethereum")
    print(f"ETH balance for {eth_address}: {balance}")

    # Test chain info
    print("\nTesting chain info...")
    chain_info = await read_chain_info(network="ethereum")
    print(f"Chain info: {chain_info}")

    # Test read token balance
    print("\nTesting token balance...")
    token_address = "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984"  # UNI token address
    owner_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Example address
    token_balance = await read_token_balance(network="ethereum", token_address=token_address, address=owner_address)
    print(f"Token balance for {owner_address}: {token_balance}")
    
    # Test ENS resolution
    print("\nTesting ENS resolution...")
    ens_name = "vitalik.eth"
    resolved_address = await resolve_ens(ens_name)
    print(f"ENS {ens_name} resolves to: {resolved_address}")
    
    # Test token balance
    print("\nTesting token balance...")
    token_address = "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984"  # UNI token address
    wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Example address
    token_balance = await get_token_balance(token_address, wallet_address)
    print(f"Token balance for {wallet_address}: {token_balance}")

if __name__ == "__main__":
    asyncio.run(main())