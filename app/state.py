# app/state.py
import os
from typing import TypedDict
from langgraph.checkpoint.postgres import PostgresSaver
from psycopg_pool import ConnectionPool
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    competitor: str
    research_data: str
    extracted_pricing: dict
    comparison_result: str
    final_report: str

DB_URL = os.getenv("SUPABASE_DB_URL")

connection_kwargs = {
    "autocommit": True,
    "prepare_threshold": None, 
}

pool = ConnectionPool(conninfo=DB_URL, max_size=20, kwargs=connection_kwargs)

# We initialize it, but we REMOVE .setup() because we did it manually
checkpointer = PostgresSaver(pool)

print("✅ Supabase checkpointer ready (Schema assumed existing).")
