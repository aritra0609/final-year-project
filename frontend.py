#Step 1:Setup UI with Streamlit
import streamlit as st

st.set_page_config(page_title="RAG Web APP", layout="wide")
st.title("RAG-based Web Search Application by Aritra Ganguly and Toufique Islam")
st.write("Ask me a question and I will try to answer it.")
system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mistral-saba-24b"]
provider=st.radio("Select Provider:", ("Groq"))
if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)

allow_web_search=st.checkbox("Allow Web Search")
user_query=st.text_area("Ask your query: ", height=150, placeholder="Let's Chat!")
API_URL="http://127.0.0.1:9999/chat"
#Step 2: Connect backend via URL
if st.button("Ask Agent!"):
    if user_query.strip():
        #Step2: Connect with backend via URL
        import requests

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Response")
                st.markdown(f"{response_data}")