from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agent import app
from uuid import uuid4

api = FastAPI()

class ResearchRequest(BaseModel):
    competitor: str
    thread_id: str = "default_job"

@api.post("/research")
async def run_research(request: ResearchRequest):
    config = {"configurable": {"thread_id": request.thread_id}}
    initial_state = {"competitor": request.competitor}
    
    try:
        # Stream the results
        result = None
        async for event in app.astream(initial_state, config=config):
            result = event
        return {"status": "success", "last_event": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
