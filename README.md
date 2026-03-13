🧠AI-Powered Web Search Assistant with RAG

A blazing-fast, real-time AI question answering system powered by Groq, LangChain, and Tavily, with a modern FastAPI + Streamlit stack.

🚀 Features
🔍 RAG pipeline with optional live web search (Tavily)

⚡ Ultra-fast inference via Groq for near-instant responses

🧠 LangChain internally uses LangGraph for state management and agent orchestration. So while I didn’t write a graph myself, my agent follows a ReAct pattern under the hood.

🌐 Full-stack: Streamlit frontend + FastAPI backend

✅ Validated input with Pydantic, clean env with pipenv

🛠️ Tech Stack

LLMs: Groq-hosted models

Inference: Groq API

Tools: Tavily Search API for live retrieval

Memory & Agents: LangChain (internally powered by LangGraph for state management, no explicit graph nodes)

UI: Streamlit for frontend

API: FastAPI + Uvicorn for backend

Validation: Pydantic models for request validation

Environment Management: pipenv for dependency and environment control

📌 How It Works
User sends a query via Streamlit (with optional web search).

FastAPI routes it to an AI agent (LangGraph ReAct).

If allowed, Tavily fetches live data; Groq accelerates the LLM.

Final answer is returned to the UI.

📈 Example

POST /chat
{
  "query": "Latest update on GPT-4.5?",
  "allow_search": true
}
Live Link : https://final-year-project-tiag.streamlit.app/
