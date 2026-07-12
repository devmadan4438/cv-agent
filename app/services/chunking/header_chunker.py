from langchain_core.documents import Document
from .base import BaseChunker
from app.schemas.metadata import Header
from langsmith import traceable

class HeaderChunker(BaseChunker):

    @traceable(
        name="Header chunk",
        
    )
    def chunk(self, header: Header):

        content = f"""
            name: {header.name}

            email: {header.email}

            phone: {header.phone}

            linkedin: {header.linkedin}

            github: {header.github}
            
            portfolio: {header.portfolio}
            """

        metadata = {

            "type": "header",
            "name": {header.name},
            "email": {header.email},
            "phone": {header.phone},
            "linkedin": {header.linkedin},
            "github": {header.github},
            "portfolio": {header.portfolio}
        }

        return [
            Document(
                page_content=content.strip(),
                metadata=metadata
            )
        ]