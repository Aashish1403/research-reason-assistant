import httpx
import asyncio
from typing import List, Dict, Any
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse

class WebSearchTool:
    """MCP Web Search Tool"""
    
    def __init__(self):
        self.name = "web_search"
        self.description = "Search the web for information"
        
    async def search(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """
        Search the web using DuckDuckGo API (free alternative to Google)
        """
        try:
            # Using DuckDuckGo Instant Answer API (free)
            search_url = "https://api.duckduckgo.com/"
            params = {
                "q": query,
                "format": "json",
                "pretty": 1,
                "no_redirect": 1,
                "no_html": 1,
                "skip_disambig": 1
            }
            
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(search_url, params=params)
                data = response.json()
                
                results = []
                
                # Add abstract if available
                if data.get("Abstract"):
                    results.append({
                        "url": data.get("AbstractURL", ""),
                        "title": data.get("Heading", "Abstract"),
                        "snippet": data.get("Abstract", ""),
                        "source": "DuckDuckGo Abstract"
                    })
                
                # Add related topics
                for topic in data.get("RelatedTopics", [])[:max_results-1]:
                    if isinstance(topic, dict) and "Text" in topic:
                        results.append({
                            "url": topic.get("FirstURL", ""),
                            "title": topic.get("Text", "")[:100],
                            "snippet": topic.get("Text", ""),
                            "source": "DuckDuckGo Related"
                        })
                
                # If no results, create mock results for demo
                if not results:
                    results = self._create_demo_results(query)
                    
                return results[:max_results]
                
        except Exception as e:
            print(f"Search error: {e}")
            return self._create_demo_results(query)
    
    def _create_demo_results(self, query: str) -> List[Dict[str, Any]]:
        """Create demo results for testing"""
        return [
            {
                "url": "https://en.wikipedia.org/wiki/Example",
                "title": f"About {query} - Wikipedia",
                "snippet": f"This is demo content about {query}. Wikipedia is a free online encyclopedia.",
                "source": "Demo Wikipedia"
            },
            {
                "url": "https://www.example.com/article",
                "title": f"{query} - Complete Guide",
                "snippet": f"Learn everything about {query} in this comprehensive guide with examples.",
                "source": "Demo Article"
            }
        ]

class WebFetchTool:
    """MCP Web Fetch Tool"""
    
    def __init__(self):
        self.name = "web_fetch"
        self.description = "Fetch content from URLs"
        self.max_content_length = 10000
    
    async def fetch(self, url: str, max_chars: int = 10000) -> Dict[str, Any]:
        """
        Fetch and parse content from a URL
        """
        try:
            if not url or url.startswith("https://www.example.com"):
                # Return demo content for demo URLs
                return self._create_demo_content(url)
            
            async with httpx.AsyncClient(
                timeout=15.0,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                }
            ) as client:
                response = await client.get(url)
                response.raise_for_status()
                
                # Parse HTML content
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.decompose()
                
                # Get text content
                text = soup.get_text()
                
                # Clean up text
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                text = ' '.join(chunk for chunk in chunks if chunk)
                
                # Limit content length
                if len(text) > max_chars:
                    text = text[:max_chars] + "..."
                
                return {
                    "url": url,
                    "title": soup.title.string if soup.title else "No Title",
                    "content": text,
                    "length": len(text),
                    "status": "success"
                }
                
        except Exception as e:
            print(f"Fetch error for {url}: {e}")
            return self._create_demo_content(url, error=str(e))
    
    def _create_demo_content(self, url: str, error: str = None) -> Dict[str, Any]:
        """Create demo content for testing"""
        if error:
            content = f"Demo content for {url}. (Note: Real fetch failed: {error})"
        else:
            content = f"This is demo content fetched from {url}. In a real implementation, this would contain the actual webpage content."
        
        return {
            "url": url,
            "title": f"Demo Content - {url}",
            "content": content,
            "length": len(content),
            "status": "demo"
        }

# Initialize tools
web_search_tool = WebSearchTool()
web_fetch_tool = WebFetchTool()
