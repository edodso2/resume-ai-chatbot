import gradio as gr
from utils.env import load_env
from utils.database import initialize_database
from utils.chatbot import create_conversation_chain

MODEL = "gpt-4o-mini"
db_name = "vector_db"

# Load secrets
load_env()

# Initialze DB for RAG
vector_store = initialize_database(db_name)

# Create LangChain conversation chain
conversation_chain = create_conversation_chain(MODEL, vector_store)

# Chat function for UI to invoke the conversation chain
def chat(message, history):
    result = conversation_chain.invoke({"question": message})
    return result["answer"]

# Simple chat UI
demo = gr.ChatInterface(
    chat,
    title="Simple Chat Assistant",
    textbox=gr.Textbox(placeholder="Ask me anything..."),
)

if __name__ == "__main__":
    demo.launch()
