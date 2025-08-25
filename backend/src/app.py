from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Chat API",
    description="FastAPI backend with PostgreSQL and LangGraph",
    version="0.1.0"
)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "chat-api"
    }