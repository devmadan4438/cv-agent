from pathlib import Path

from app.services.parser.pdf_parser import PDFParser
from app.services.parser.docx_parser import DocxParser


class ParserFactory:

    @staticmethod
    def get_parser(filename: str):

        ext = Path(filename).suffix.lower()

        if ext == ".pdf":
            return PDFParser()

        if ext == ".docx":
            return DocxParser()

        raise ValueError("Unsupported file")