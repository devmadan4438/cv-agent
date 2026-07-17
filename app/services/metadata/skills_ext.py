from .base import BaseMetadataExtractor
from app.schemas.metadata import SkillList

class SkillsExtractor(BaseMetadataExtractor):

    def __init__(self, llm):
        self.structured_llm = llm.with_structured_output(SkillList)

    def extract(self, section):

        prompt = f"""
        Extract all technical skills.

        Resume Section:

        {section.content}
        """

        result = self.structured_llm.invoke(prompt)

        return result.skills