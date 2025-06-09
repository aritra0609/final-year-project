🧠 Generative AI Chatbot with RAG (Retrieval-Augmented Generation)
🔍 Real-time, intelligent, and ultra-fast chatbot using Groq, OpenAI/Mistral, LangChain, Tavily, and FastAPI.

📌 Overview
This project builds a Generative AI Chatbot capable of producing context-aware, real-time answers using RAG (Retrieval-Augmented Generation). It blends language models with live web search, offering ultra-fast responses thanks to Groq inference and structured agent reasoning via LangGraph.

✅ Built using Python, integrates LLMs, tools, web APIs, and a full-stack deployment pipeline.

💬 Sample Queries:
• What is the latest update on OpenAI's GPT models?
• Who won the last Champions League match?
• Write SQL query to get top 3 employees by salary.

🧩 Tech Stack
Layer	Technology
Frontend	Streamlit – Chat UI with checkbox for web search
Backend	FastAPI – High-performance API server
LLMs	OpenAI GPT, Mistral – Language generation
Inference	Groq – Accelerated inference engine
Tooling	Tavily API – Real-time web search
Memory + Tools	LangChain + LangGraph ReactAgent
Server	Uvicorn – ASGI server
Validation	Pydantic – Input schema validation
Environment	pipenv – Dependency and virtualenv management

🔧 Features
✅ Retrieval-Augmented Generation (RAG) pipeline
🌐 Real-time web search with optional toggle (via Tavily API)
⚡ Ultra-fast inference using Groq’s hardware-accelerated backend
🧠 Step-by-step reasoning via LangGraph ReactAgent
🛡️ Pydantic validation for safe and reliable API usage
🖥️ Streamlit UI for interactive chatting
🔁 Full frontend-backend integration

🛠️ Project Structure

├── ai_agent.py          # Core logic: model, tools, LangGraph agent
├── backend.py           # FastAPI backend, input validation, routing
├── frontend.py          # Streamlit UI, handles user chat and checkboxes
├── Pipfile              # Dependencies and virtualenv definition
├── README.md            # You’re here!
📈 How It Works

User inputs a query in Streamlit, and optionally enables “Web Search”.
FastAPI receives the query and passes it to the AI agent.
LangGraph ReactAgent decides how to respond:
Uses Tavily tool if needed (based on checkbox)
Uses Groq-accelerated LLM (OpenAI/Mistral)
Or combines both (RAG)
Final response is returned to the frontend UI.

📌 Key Components
🔹 Groq
Hardware-accelerated inference engine for ultra-low latency LLM output.

🔹 OpenAI / Mistral
Supports both proprietary (GPT) and open-source (Mistral) models.

🔹 Tavily API
Enables real-time search; useful for time-sensitive or web-based queries.

🔹 LangChain + LangGraph
Memory, reasoning steps, and tool orchestration via ReactAgent flow.

🔹 FastAPI + Uvicorn
Backend to serve AI responses with speed, stability, and validation.

🧠 Learnings
Implemented a full-stack AI app with custom tool orchestration.
Understood LangChain + LangGraph agent framework deeply.
Integrated real-time search, validation, and modular API backend.
Used Groq for optimizing latency-sensitive inference.

🎯 Future Enhancements
🎙️ Add voice input/output
🌍 Enable multilingual support
🖼️ Add image input (multimodal)
👤 Add user profile personalization

🧪 API Endpoints

POST /chat
{
  "query": "Who is the president of India?",
  "allow_search": true
}
Response:
{
  "response": "As of June 2025, the President of India is..."
}
