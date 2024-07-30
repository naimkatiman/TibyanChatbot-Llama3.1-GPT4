
# LLM-Chatbot-Tibyan Everything

This is a simple chatbot built with Llama 3.1 405B.

## How to Run the Chatbot

Follow these steps to set up and run the Llama 3.1 405B chatbot:

### Clone the GitHub Repository

```bash
git clone https://github.com/naimkatiman/TibyanChatbot-Llama3.1-GPT4.git
cd llm-chatbot
```

### Set Up a Virtual Environment

It's recommended to use a virtual environment to manage your project dependencies. Here are the steps:

#### For Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS and Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install the Required Dependencies

```bash
pip install -r requirements.txt
```

### Obtain a Fireworks API Key

1. Sign up for an account at [Fireworks AI](https://www.fireworks.ai).
2. Generate an API key from your account dashboard.

### Edit the Environment File

Rename `.env.sample` to `.env` and add your API keys:

```
OPENAI_API_KEY=your_openai_api_key
FIREWORKS_API_KEY=your_fireworks_api_key
```

### Run the Streamlit App

```bash
streamlit run llama3_chat.py
```

### Start Chatting

1. When the app opens in your browser:
2. Enter your Fireworks API key in the sidebar.
3. Start chatting with the Llama 3.1 405B model!

> **Note:** Keep your API key confidential and do not share it publicly.

---


Please ensure to upload the actual images (`screenshot.png` and `another_image_or_logo.png`) to the `assets` directory in your repository. If you have specific images you would like to use, please upload them, and I can assist you with incorporating them correctly.
