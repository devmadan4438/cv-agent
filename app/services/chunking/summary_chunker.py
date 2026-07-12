from langchain_core.documents import Document
from .base import BaseChunker
from app.schemas.metadata import Summary
from langsmith import traceable

class SummaryChunker(BaseChunker):

    @traceable(
        name="Summary chunk"
    )
    def chunk(self, summary: Summary):

        content = f"""
            summary: {summary.summary}
            """

        metadata = {
            "type": "summary",
            "summary" : "summary"
        }

        return [
            Document(
                page_content=content.strip(),
                metadata=metadata
            )
        ]