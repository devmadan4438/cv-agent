from .base import BaseMetadataExtractor
from app.schemas.metadata import (
    HeaderList
)

class HeaderExtractor(BaseMetadataExtractor):
     
    def __init__(self, llm):
        self.structured_llm = llm.with_structured_output(HeaderList)

    def extract(self, section):
        prompt = f"""
        You are an expert resume parser.

        Extract the candidate's contact information from the resume header.

        Extract:
        - Full Name
        - Email
        - Phone Number
        - Location
        - LinkedIn URL
        - GitHub URL
        - Portfolio/Personal Website

        Rules:
        - Return null for missing fields.
        - Do not infer or guess values.
        - Ignore other resume sections.

        Resume Header:

        {section.content}
        """

        result = self.structured_llm.invoke(prompt)

        return result.headers