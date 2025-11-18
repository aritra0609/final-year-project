import streamlit as st
import requests

st.set_page_config(page_title="RAG Web APP", layout="wide")
st.title("RAG-based Web Search Application by Aritra Ganguly and Toufique Islam")

system_prompt = st.text_area("Define your AI Agent:", height=70, placeholder="Type your system prompt here...")
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "qwen/qwen3-32b"]
provider = st.radio("Select Provider:", ("Groq",))
selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)

allow_web_search = st.checkbox("Allow Web Search")
user_query = st.text_area("Ask your query:", height=150, placeholder="Let's Chat!")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if not user_query.strip():
        st.warning("Please enter a query first.")
    else:
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }
        try:
            response = requests.post(API_URL, json=payload)
            response.raise_for_status()
            data = response.json()

            # Extract the last AI message
            ai_message = ""
            if "messages" in data:
                for msg in reversed(data["messages"]):
                    if msg.get("type") == "ai":
                        ai_message = msg.get("content", "")
                        break
            elif "response" in data and "messages" in data["response"]:
                for msg in reversed(data["response"]["messages"]):
                    if msg.get("type") == "ai":
                        ai_message = msg.get("content", "")
                        break

            if ai_message:
                st.subheader("AI Response")
                st.markdown(ai_message)
            else:
                st.warning("No AI response found.")

        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
