from openai import OpenAI
import streamlit as st

# Sidebar setup
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    model_choice = st.selectbox("Select GPT model:", options=["gpt-4o", "gpt-4o-mini"], index=0)  # Add selector for model
  

# Chatbot UI
st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display message history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input and OpenAI API interaction
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # Create OpenAI client and send message
    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Use selected model from the sidebar
    response = client.chat.completions.create(model=model_choice, messages=st.session_state.messages)
    
    # Get and display assistant's response
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
