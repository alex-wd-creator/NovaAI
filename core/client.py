from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")

if not BASE_URL:
    raise RuntimeError("Falta BASE_URL en el archivo .env")

if not API_KEY:
    raise RuntimeError("Falta API_KEY en el archivo .env")

if not MODEL:
    raise RuntimeError("Falta MODEL en el archivo .env")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)