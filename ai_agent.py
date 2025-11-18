# ai_agent.py
import os
from typing import List

from langchain.agents import create_agent  
from langchain_community.tools.tavily_search import TavilySearchResults

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

# Load API keys (set these in your env)
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")


def get_response_from_ai_agent(
    llm_id: str,
    messages: List[str],
    allow_search: bool,
    system_prompt: str,
    provider: str
):
    # Select LLM
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id, openai_api_key=OPENAI_API_KEY)
    else:
        raise ValueError("Invalid provider")

    # Tools
    tools = [TavilySearchResults(max_results=2, api_key=TAVILY_API_KEY)] if allow_search else []

    # Create agent (LangChain v1 API) :contentReference[oaicite:1]{index=1}  
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )

    # Prepare conversation (flat)
    input_text = "\n".join(messages)

    # Run and get response
    response = agent.invoke({"messages": [{"role": "user", "content": input_text}]})
    return response
