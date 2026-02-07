import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")

if not API_URL:
    raise RuntimeError("API_URL não definida")
