from dotenv import load_dotenv
from .setting import settings
import os

CHAT_DIR = "data/chat_log"
VECTOR_DIR = "data/vectorstore"

os.makedirs(CHAT_DIR, exist_ok=True)
os.makedirs(VECTOR_DIR, exist_ok=True)

# Set Langsmith in env
os.environ["LANGSMITH_TRACING"] = settings.LANGSMITH_TRACING
os.environ["LANGSMITH_API_KEY"] = settings.LANGSMITH_API_KEY
os.environ["LANGSMITH_PROJECT"] = settings.LANGSMITH_PROJECT