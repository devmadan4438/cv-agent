from langchain_groq import ChatGroq
from app.core.setting import settings
from .base import LLMBase
import logging

logger = logging.getLogger(__name__)

class ChatGroqLLM(LLMBase):
    
    def __init__(self):
        self.client = ChatGroq(
            api_key= settings.GROQ_API_KEY,
            temperature=0.2,
            model=settings.GROQ_MODEL
        )
        logger.info("GROQ initialized successfully")

    def get_client(self):
        return self.client
