from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

modelId="llama-3.1-8b-instant"

def get_llm():
    llm = ChatGroq(model=modelId, api_key=os.getenv("GROQ_API_KEY"))
    return llm