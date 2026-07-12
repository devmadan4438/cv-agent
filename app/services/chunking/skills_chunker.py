from langchain_core.documents import Document
from .base import BaseChunker
from app.schemas.metadata import SkillList
from langsmith import traceable
import logging

# logger
logger = logging.getLogger(__name__)

class SkillsChunker(BaseChunker):

    @traceable(
        name="skill chunk"
    )
    def chunk(self, skills: SkillList):
        logger.info("start skill chunking")
        content = "\n".join(
            skill.name
            for skill in skills.skills
        )
        logger.info(f"skill chunking done of length {len(skills.skills)}")
        
        return [

            Document(
                page_content=content,

                metadata={
                    "type": "skills"
                }
            )
        ]