from abc import ABC, abstractmethod
from langchain_core.documents import Document

class BaseChunker(ABC):

    @abstractmethod
    def chunk(self, entity) -> list[Document]:
        pass