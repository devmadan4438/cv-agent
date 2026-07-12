import fitz
from langsmith import traceable
import logging

# service
from app.services.parser.base import BaseParser
from app.schemas.document import (
    ParsedDocument,
    Page,
    TextLine,
)

# logger
logger = logging.getLogger(__name__)

class PDFParser(BaseParser):

    @traceable(
        name="PDF Parser",
        run_type="parser",
    )
    def parse(self, file_path: str) -> ParsedDocument:
        logger.info("Parsing PDF: %s", file_path)

        pdf = fitz.open(file_path)

        pages = []

        for page_number, page in enumerate(pdf, start=1):

            page_dict = page.get_text("dict")

            lines = []

            for block in page_dict["blocks"]:

                if block["type"] != 0:
                    continue

                for line in block["lines"]:

                    spans = line["spans"]

                    text = "".join(
                        span["text"] for span in spans
                    ).strip()

                    if not text:
                        continue

                    font_size = max(
                        span["size"] for span in spans
                    )

                    font = spans[0]["font"]

                    is_bold = any(
                        "bold" in span["font"].lower()
                        or span["flags"] & 16
                        for span in spans
                    )

                    lines.append(
                        TextLine(
                            text=text,
                            page=page_number,
                            bbox=tuple(line["bbox"]),
                            font=font,
                            font_size=font_size,
                            is_bold=is_bold,
                        )
                    )

            lines.sort(
                key=lambda x: (
                    x.bbox[1],
                    x.bbox[0],
                )
            )

            pages.append(
                Page(
                    page_number=page_number,
                    text=page.get_text(),
                    lines=lines,
                )
            )

        pdf.close()

        logger.info(
            "Parsed %d pages from %s",
            len(pages),
            file_path,
        )

        return ParsedDocument(
            filename=file_path,
            total_pages=len(pages),
            pages=pages,
        )