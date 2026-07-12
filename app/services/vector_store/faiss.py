from typing import List, Optional
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_community.vectorstores import FAISS
from app.core.setting import settings
import logging

# logger
logger = logging.getLogger(__name__)

class FAISSService:

    def __init__(self, embeddings: Embeddings):
        self.embeddings = embeddings
        self.db: FAISS | None = None

    def build(self, documents: List[Document]) -> "FAISSService":
        if not documents:
            raise ValueError("No documents provided to build the FAISS index.")

        self.db = FAISS.from_documents(
            documents,
            self.embeddings,
        )
        return self

    def save(self, path: str) -> "FAISSService":
        if self.db is None:
            raise ValueError("FAISS index has not been built or loaded.")

        self.db.save_local(path)
        return self

    def load(self, path: str) -> "FAISSService":
        self.db = FAISS.load_local(
            path,
            self.embeddings,
            allow_dangerous_deserialization=True,
        )
        logging.info("FAISS loaded successfully")
        return self

    def get_retriever(self, k: int = settings.TOP_K_RETRIEVER):
        if self.db is None:
            raise ValueError("FAISS index has not been built or loaded.")

        return self.db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k},
        )
    
    def search(self, query: str, k: int = settings.TOP_K_RETRIEVER, filter: Optional[dict] = None,) -> List[Document]:
        logging.info("FAISS start searching")
        if self.db is None:
            raise ValueError("FAISS index has not been built or loaded.")

        return self.db.similarity_search(query, k=k,filter=filter)