from .base import BaseMetadataExtractor
from app.schemas.metadata import (
    EducationList
)

class EducationExtractor(BaseMetadataExtractor):

    def __init__(self, llm):

        self.structured_llm = llm.with_structured_output(
            EducationList
        )

    def extract(self, section):

        prompt = f"""
        Extract education details.

        Resume Section

        {section.content}
        """

        result = self.structured_llm.invoke(prompt)
        return result.educations