import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Carrega variáveis de ambiente
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
load_dotenv(os.path.join(BASE_DIR, 'src', '.env'))

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("⚠️ OPENAI_API_KEY não encontrado no .env")

def load_llm(id_model="deepseek-r1-distill-llama-70b", temperature=1):
    llm = ChatGroq(
      model=id_model,
      temperature=temperature,
      max_tokens=None,
      timeout=None,
      max_retries=2,
    )

    return llm
