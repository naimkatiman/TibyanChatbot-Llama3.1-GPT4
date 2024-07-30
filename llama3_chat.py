import os
from dotenv import load_dotenv
import streamlit as st
from streamlit_chat import message
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
fireworks_api_key = os.getenv('FIREWORKS_API_KEY')

# Page config
st.set_page_config(page_title="Tibyan Everything", page_icon="🌟", layout="wide")

# Import external CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Import external JavaScript
def load_js(file_name):
    with open(file_name) as f:
        st.components.v1.html(f'<script>{f.read()}</script>', height=0)

# Load external files
load_css('css/style.css')
load_js('js/script.js')

# Custom CSS for header and footer
st.markdown("""
<style>
.header-container {
    display: flex;
    align-items: center;
    padding: 1rem 0;
}
.header-logo {
    width: 30px;
    height: 30px;
    margin-right: 1rem;
}
.header-title {
    font-size: 2.5rem;
    color: #333;
}
.footer {
    background-color: #f0f0f0;
    color: #333;
    text-align: center;
    padding: 10px 0;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <h1 class="header-title">Tibyan Everything</h1>
</div>
""", unsafe_allow_html=True)
st.image('assets/tibyanlogo.png', width=50)

# Sidebar
with st.sidebar:
    st.title("🌟 Tibyan Everything")
    st.markdown("Unlock infinite knowledge with your AI sidekick")
    api_key = st.text_input("Enter your Fireworks API Key", type="password", value=fireworks_api_key)

# Initialize session state variables
if 'buffer_memory' not in st.session_state:
    st.session_state.buffer_memory = ConversationBufferWindowMemory(k=3, return_messages=True)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you today?"}
    ]
if "conversation" not in st.session_state:
    st.session_state.conversation = None

# Chat interface
if api_key:
    if st.session_state.conversation is None:
        llm = ChatOpenAI(
            model="accounts/fireworks/models/llama-v3p1-405b-instruct",
            openai_api_key=api_key,
            openai_api_base="https://api.fireworks.ai/inference/v1"
        )
        st.session_state.conversation = ConversationChain(
            memory=st.session_state.buffer_memory,
            llm=llm
        )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Your question"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.conversation.predict(input=prompt)
                st.write(response)
                message = {"role": "assistant", "content": response}
                st.session_state.messages.append(message)
else:
    st.warning("Please enter your Fireworks API Key in the sidebar to start the chat.")

# Footer (place this at the very end of your script)
st.markdown("""
<div class="footer">
    <p>Powered by Llama 3.1 (405B) model | Made with ❤️ | <a href="https://www.naimkatiman.com" target="_blank">www.naimkatiman.com</a></p>
</div>
""", unsafe_allow_html=True)
