from app.infra.llm.chatGroq import ChatGroqLLM

class LLMFactory:
    @staticmethod
    def get_client(provider: str = 'groq'):
        if provider == 'groq':
            return ChatGroqLLM().get_client()
