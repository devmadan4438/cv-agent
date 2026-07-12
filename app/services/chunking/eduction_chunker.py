from langchain_core.documents import Document
from .base import BaseChunker
from app.schemas.metadata import Education
from langsmith import traceable

class EducationChunker(BaseChunker):

    @traceable(
        name="Education chunk" 
    )
    def chunk(self, edu: Education):

        content = f"""
            institute: {edu.institution}

            degree: {edu.degree}

            grade: {edu.grade}

            start_date: {edu.start_date}

            end_date: {edu.end_date}
            """

        metadata = {

            "type": "education",

            "institute": {edu.institution},

            "degree": {edu.degree},

            "grade": {edu.grade},

            "start_date": {edu.start_date},

            "end_date": {edu.end_date}
        }

        return [
            Document(
                page_content=content.strip(),
                metadata=metadata
            )
        ]