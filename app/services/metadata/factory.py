from .education_ext import EducationExtractor
from .experience_ext import ExperienceExtractor
from .skills_ext import SkillsExtractor
from .project_ext import ProjectExtractor
from .header_ext import HeaderExtractor
from .summary_ext import SummaryExtractor

from app.infra.llm.factory import LLMFactory

llm = LLMFactory.get_client()

class MetadataExtractorFactory:

    mapping = {
        "header": HeaderExtractor(llm = llm),
        "summary": SummaryExtractor(),
        "experience": ExperienceExtractor(llm=llm),
        "skills": SkillsExtractor(llm=llm),
        "projects": ProjectExtractor(llm=llm),
        "education": EducationExtractor(llm=llm),
    }

    @classmethod
    def get(cls, section_name):
        return cls.mapping.get(section_name)