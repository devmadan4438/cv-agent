from .base import BaseEmbedding
from langchain_community.embeddings import OllamaEmbeddings
from app.core.setting import settings
import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning

warnings.filterwarnings(
    "ignore",
    category=LangChainDeprecationWarning,
)

class NomicEmbedding(BaseEmbedding):
    
    def get_embeddings(self):
        return OllamaEmbeddings(
            model= settings.EMBEDDING_MODEL
        )