from pydantic import BaseModel

class TextLine(BaseModel):
    text: str
    page: int
    bbox: tuple[float, float, float, float]
    font: str
    font_size: float
    is_bold: bool


class Page(BaseModel):
    page_number: int
    text: str
    lines: list[TextLine]


class ParsedDocument(BaseModel):
    filename: str
    total_pages: int
    pages: list[Page]