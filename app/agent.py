import os
from langgraph.graph import StateGraph, END
from app.state import AgentState, checkpointer
from langchain_groq import ChatGroq

# Initialize LLM
llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

# 1. Node Functions
def research_node(state: AgentState):
    print("--- STEP 1: RESEARCHING ---")
    # Simulate research (In production, replace with Tavily Search)
    return {"research_data": f"Competitor {state['competitor']} offers pricing at $99/mo."}

def extract_node(state: AgentState):
    print("--- STEP 2: EXTRACTING ---")
    return {"extracted_pricing": {"price": 99, "currency": "USD"}}

def compare_node(state: AgentState):
    print("--- STEP 3: COMPARING ---")
    # Simulate DB comparison
    return {"comparison_result": "Competitor is $10 cheaper than our base plan."}

def draft_node(state: AgentState):
    print("--- STEP 4: DRAFTING REPORT ---")
    return {"final_report": f"Strategy Report: {state['comparison_result']}"}

# 2. Build the Graph
workflow = StateGraph(AgentState)

workflow.add_node("research", research_node)
workflow.add_node("extract", extract_node)
workflow.add_node("compare", compare_node)
workflow.add_node("draft", draft_node)

workflow.set_entry_point("research")
workflow.add_edge("research", "extract")
workflow.add_edge("extract", "compare")
workflow.add_edge("compare", "draft")
workflow.add_edge("draft", END)

# 3. Compile with Checkpointer
app = workflow.compile(checkpointer=checkpointer)
