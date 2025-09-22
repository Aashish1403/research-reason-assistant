from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import os
from dotenv import load_dotenv
from app.services.orchestrator import orchestrator

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Research & Reason Assistant API",
    description="Intelligent research assistant with multi-agent reasoning",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

class Citation(BaseModel):
    url: str
    title: str
    snippet: str

class TraceEntry(BaseModel):
    timestamp: str
    agent: str
    action: str
    tool: str
    input: Dict[str, Any]
    output: Dict[str, Any]
    status: str

class ResearchResponse(BaseModel):
    answer: str
    reasoning: str
    citations: List[Citation]
    trace: List[TraceEntry]

@app.get("/")
async def root():
    return {
        "message": "Research & Reason Assistant API",
        "status": "running",
        "version": "1.0.0",
        "agents": "CrewAI Multi-Agent System Active"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "agents": "operational",
        "tools": "mcp_active"
    }

@app.post("/api/ask")
async def ask_question(request: QueryRequest):
    """
    Main endpoint for processing research questions with CrewAI agents
    """
    try:
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        # Process with CrewAI agents
        result = await orchestrator.process_query(request.question)
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 8000)),
        reload=True
    )
