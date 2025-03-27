#!/usr/bin/env python3
import asyncio
from src.simple_mcp_client import add_numbers, get_greeting, get_current_time

async def main():
    """Example usage of the client"""
    print("Testing simple mcp client...")
    
    # Test addNumbers
    print("\nTesting addNumbers...")
    result = await add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    # Test getGreeting
    print("\nTesting getGreeting...")
    greeting = await get_greeting("World")
    print(f"Greeting: {greeting}")
    
    # Test getCurrentTime
    print("\nTesting getCurrentTime...")
    current_time = await get_current_time()
    print(f"Current time: {current_time}")

if __name__ == "__main__":
    asyncio.run(main())