from langchain_core.documents import Document
from .base import BaseChunker
from app.schemas.metadata import Experience
from langsmith import traceable

class ExperienceChunker(BaseChunker):

    @traceable(
        name="Experience chunk"
    )
    def chunk(self, exp: Experience):

        content = f"""
            Company: {exp.company}

            Client: {exp.client}

            Role: {exp.role}

            Responsibilities:

            {chr(10).join(exp.responsibilities)}

            Skills:

            {", ".join(exp.skills)}
            """

        metadata = {

            "type": "experience",

            "company": exp.company,

            "client": exp.client,

            "role": exp.role,

            "skills": exp.skills
        }

        return [
            Document(
                page_content=content.strip(),
                metadata=metadata
            )
        ]