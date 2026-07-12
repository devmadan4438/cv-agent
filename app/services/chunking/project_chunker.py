from langchain_core.documents import Document
from .base import BaseChunker
from app.schemas.metadata import Project

class ProjectChunker(BaseChunker):

    def chunk(self, prj: Project):

        content = f"""
            name: {prj.name}

            description: {prj.description}

            role: {prj.role}

            start_date: {prj.start_date}

            end_date: {prj.end_date}
            """

        metadata = {

            "type": "project",

            "name": {prj.name},

            "description": {prj.description},

            "role": {prj.role},

            "start_date": {prj.start_date},

            "end_date": {prj.end_date}
        }

        return [
            Document(
                page_content=content.strip(),
                metadata=metadata
            )
        ]