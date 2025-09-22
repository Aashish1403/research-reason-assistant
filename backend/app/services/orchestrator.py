from typing import Dict, Any
import sys
import os
from datetime import datetime

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, backend_dir)

try:
    from app.agents.research_agents import research_agents
    AGENTS_AVAILABLE = True
    print("✅ Working research agents loaded successfully")
except ImportError as e:
    print(f"❌ Research agents not available: {e}")
    AGENTS_AVAILABLE = False

class ResearchOrchestrator:
    """Main orchestrator for the research system"""
    
    def __init__(self):
        self.agents_available = AGENTS_AVAILABLE
        if self.agents_available:
            self.agents = research_agents
        print(f"🚀 Orchestrator initialized - Agents: {'✅ Available' if self.agents_available else '❌ Fallback mode'}")
    
    async def process_query(self, question: str) -> Dict[str, Any]:
        """Process a user query using research agents or fallback"""
        if self.agents_available:
            return await self._process_with_agents(question)
        else:
            return await self._process_fallback(question)
    
    async def _process_with_agents(self, question: str) -> Dict[str, Any]:
        """Process using research agents"""
        try:
            print(f"🤖 Processing with Working Agents: {question}")
            result = await self.agents.process_question(question)
            print(f"✅ Agent processing completed")
            return result
        except Exception as e:
            print(f"❌ Agent processing failed: {e}")
            return await self._process_fallback(question, error=str(e))
    
    async def _process_fallback(self, question: str, error: str = None) -> Dict[str, Any]:
        """Fallback processing without agents"""
        error_msg = f" (Agent Error: {error})" if error else ""
        
        return {
            "answer": f"I'm working on your question: '{question}'. The system is operating in fallback mode{error_msg}.",
            "reasoning": "The system is using fallback processing while agents are being configured.",
            "citations": [
                {
                    "url": "https://crewai.com",
                    "title": "CrewAI Multi-Agent Framework",
                    "snippet": "Advanced AI agent orchestration system"
                }
            ],
            "trace": [
                {
                    "timestamp": datetime.now().isoformat(),
                    "agent": "fallback_orchestrator",
                    "action": "process_query",
                    "tool": "fallback_processor",
                    "input": {"question": question},
                    "output": {"status": "fallback_mode", "agents_available": self.agents_available},
                    "status": "success"
                }
            ]
        }

# Initialize orchestrator
print("🔄 Initializing Research Orchestrator...")
orchestrator = ResearchOrchestrator()
