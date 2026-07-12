from .base import BaseMetadataExtractor
from app.schemas.metadata import (
    ExperienceList
)

class ExperienceExtractor(BaseMetadataExtractor):
     
    def __init__(self, llm):
        self.structured_llm = llm.with_structured_output(ExperienceList)

    def extract(self, section):
        prompt = f"""
        Extract all work experiences.

        Resume Section:

        {section.content}
        """

        result = self.structured_llm.invoke(prompt)

        return result.experiences