# Resilient Agentic Workflow (Groq + LangGraph + Supabase)

An enterprise-grade, long-running AI agent that performs complex multi-step tasks with **checkpointing** and **quantitative evaluation**. 

Unlike standard LLM scripts that lose all progress if an API call fails, this system uses LangGraph and a Supabase Postgres connection to save state after every node execution. If the process crashes, it resumes exactly where it left off.

## 🏗 Architecture

The workflow executes a 4-step competitive analysis task:
1. **Research Competitor:** Uses Groq API to gather intelligence.
2. **Extract Pricing:** Forces Grok to output strict, validated JSON.
3. **Compare to DB:** A deterministic Python node that compares extracted data against internal data.
4. **Draft Strategy:** Grok drafts a final report based on the delta.

### The Stack
* **Orchestration:** [LangGraph](https://python.langchain.com/v0.1/docs/langgraph/) (State-machine framework)
* **LLM:** [Groq Cloud API ](https://console.groq.com/docs/overview)
* **State Persistence:** [Supabase](https://supabase.com/) (using LangGraph's `PostgresSaver`)
* **Evaluation:** [DeepEval](https://github.com/confident-ai/deepeval) (LLM-as-a-judge for Faithfulness and Relevance)
* **Deployment:** FastAPI hosted on Render

## ⚙️ Why this matters (The Enterprise Difference)

1. **State Persistence:** By passing a psycopg connection pool to LangGraph, the agent's memory is dumped to Supabase continuously. 
2. **Resiliency:** We simulate an intentional crash at step 3. On restart, the agent skips steps 1 and 2, retrieving the state from Supabase, and finishes the task.
3. **Evaluation over Vibes:** We don't guess if the agent did a good job. We run DeepEval test suites to generate a quantitative score (0.0 to 1.0) on hallucination rates and answer relevance.

## 🚀 Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/resilient-agent-workflow.git
cd resilient-agent-workflow
```

### 2. Install Dependancies
pip install -r requirements.txt

### 3.Environment Variables
check the .env file.

### 4. Run the API (Local)
```bash
uvicorn app.main:app --reload
```

### 5. Running the DeepEval Test Suite
To verify the accuracy of the agent's final report against the raw research context:
```bash
deepeval test run tests/test_agent.py
```

