🧠 Generative AI Chatbot with RAG
A blazing-fast, real-time AI chatbot powered by Groq, OpenAI/Mistral, LangChain, and Tavily, with a modern FastAPI + Streamlit stack.

🚀 Features
🔍 RAG pipeline with optional live web search (Tavily)

⚡ Ultra-fast inference via Groq for near-instant responses

🧠 Reasoning & tool orchestration using LangGraph ReAct Agent

🌐 Full-stack: Streamlit frontend + FastAPI backend

✅ Validated input with Pydantic, clean env with pipenv

🛠️ Tech Stack
LLMs: OpenAI / Mistral
Inference: Groq
Tools: Tavily API
Memory & Agents: LangChain + LangGraph
UI: Streamlit
API: FastAPI + Uvicorn
Validation: Pydantic
Env Mgmt: pipenv

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
