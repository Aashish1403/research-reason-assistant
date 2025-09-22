import asyncio
from app.tools.mcp_tools import web_search_tool, web_fetch_tool

async def test_tools():
    print("Testing MCP Tools...")
    
    # Test search
    print("\n1. Testing Web Search:")
    search_results = await web_search_tool.search("Python programming", max_results=3)
    for i, result in enumerate(search_results, 1):
        print(f"   {i}. {result['title']}")
        print(f"      URL: {result['url']}")
        print(f"      Snippet: {result['snippet'][:100]}...")
    
    # Test fetch
    print("\n2. Testing Web Fetch:")
    if search_results:
        fetch_result = await web_fetch_tool.fetch(search_results[0]['url'], max_chars=500)
        print(f"   Title: {fetch_result['title']}")
        print(f"   Content: {fetch_result['content'][:200]}...")
        print(f"   Status: {fetch_result['status']}")

if __name__ == "__main__":
    asyncio.run(test_tools())
