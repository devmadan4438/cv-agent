from .eduction_chunker import EducationChunker
from .skills_chunker import SkillsChunker
from .exp_chunker import ExperienceChunker
from .project_chunker import ProjectChunker
from .header_chunker import HeaderChunker
from .summary_chunker import SummaryChunker

from app.schemas.metadata import (
    Experience,
    Education,
    SkillList,
    Project,
    Header,
    Summary
)

class ChunkFactory:

    mapping = {
        Header : HeaderChunker(),
        Experience: ExperienceChunker(),
        Education: EducationChunker(),
        SkillList: SkillsChunker(),
        Project: ProjectChunker(),
        Summary: SummaryChunker()
    }

    @classmethod
    def get(cls, entity):
        return cls.mapping.get(type(entity), None)