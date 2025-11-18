# backend.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES = ["qwen/qwen3-32b", "llama-3.3-70b-versatile"]

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

app = FastAPI(title="Langgraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Model not found"}
    try:
        resp = get_response_from_ai_agent(
            llm_id=request.model_name,
            messages=request.messages,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider
        )
        return {"response": resp}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn, os
    port = int(os.environ.get("PORT", 9999))
    uvicorn.run(app, host="0.0.0.0", port=port)
