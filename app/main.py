from app.agent import app
from uuid import uuid4

def run_agent(competitor_name: str):
    # This thread_id is the "key" to your persistence. 
    # If you restart, use the SAME thread_id to resume.
    config = {"configurable": {"thread_id": "job_001"}}
    
    initial_state = {"competitor": competitor_name}
    
    # Run the agent
    print(f"Starting agent for {competitor_name}...")
    for event in app.stream(initial_state, config=config):
        print(event)

if __name__ == "__main__":
    run_agent("AcmeCorp")
