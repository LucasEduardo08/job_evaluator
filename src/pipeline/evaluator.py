from src.agents.resume_agent import load_llm
import json
from langchain_core.output_parsers import StrOutputParser
from src.prompts.prompts import prompt_template, prompt_score
import re



def analyze_resume(cv: str, job: dict):

    score_prompt = f"{prompt_score}\n\nCurrículo:\n{cv}\n\nVaga:\n{job}"
    llm = load_llm()
    score_response = llm.invoke(score_prompt)

    return {"score": score_response.content.strip()}
