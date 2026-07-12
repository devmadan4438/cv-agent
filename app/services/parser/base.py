from abc import ABC, abstractmethod
from app.schemas.document import ParsedDocument


class BaseParser(ABC):

    @abstractmethod
    def parse(self, file_path: str) -> ParsedDocument:
        pass