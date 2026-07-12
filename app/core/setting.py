from typing import Literal
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    ENV: Literal["development", "staging", "production"] = Field(
        default="development", alias="ENVIRONMENT"
    )
    PORT: int = Field(default=5000, alias="PORT")
    
    # LLM
    GROQ_API_KEY: str = Field(default="", alias="GROQ_API_KEY")
    GROQ_MODEL: str = Field(alias="GROQ_MODEL", default="llama-3.3-70b-versatile")
    
    # AI
    EMBEDDING_MODEL: str = Field(default="nomic-embed-text", alias="EMBEDDING_MODEL")
    
    # RETRIEVER
    TOP_K_RETRIEVER: int = Field(default=5, alias="TOP_K_RETRIEVER")

    # Langsmith
    LANGSMITH_API_KEY: str  = Field(default="", alias="LANGSMITH_API_KEY")
    LANGSMITH_TRACING: bool = Field(default=False, alias="LANGSMITH_TRACING")
    LANGSMITH_PROJECT: str  = Field(default="Boundaryless", alias="LANGSMITH_PROJECT")

settings = Settings()

