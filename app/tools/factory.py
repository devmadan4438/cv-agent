from .resume_projects import ResumeProject
from .resume_skills import ResumeSkills
from .resume_summary import ResumeSummary
from .resume_experience import ResumeExperience
from .resume_search import ResumeSearch

class ToolFactory:
    def __init__(self, faiss):

        self.faiss = faiss

    def get_tools(self):

        return [
            ResumeSearch(self.faiss).get_tool(),
            ResumeProject(self.faiss).get_tool(),
            ResumeSkills(self.faiss).get_tool(),
            ResumeSummary(self.faiss).get_tool(),
            ResumeExperience(self.faiss).get_tool()
        ]
    