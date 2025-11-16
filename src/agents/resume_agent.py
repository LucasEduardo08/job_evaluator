from langchain_groq import ChatGroq
from src.config import GROQ_API_KEY


def load_llm(id_model="openai/gpt-oss-120b", temperature=1):
    llm = ChatGroq(
      model=id_model,
      temperature=temperature,
      max_tokens=None,
      timeout=None,
      max_retries=2,
    )

    return llm
