from datetime import date
from pydantic import BaseModel

class Experience(BaseModel):
    company: str | None = None
    client: str | None = None
    role: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    responsibilities: list[str] = []
    skills: list[str] = []

class ExperienceList(BaseModel):
    experiences: list[Experience]

class Skill(BaseModel):
    name: str
    category: str | None = None


class SkillList(BaseModel):
    skills: list[Skill]

class Education(BaseModel):
    degree: str | None = None
    institution: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    grade: str | None = None

class EducationList(BaseModel):
    educations: list[Education]

class Project(BaseModel):
    name: str | None = None
    description: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    role: str | None = None

class ProjectList(BaseModel):
    projects: list[Project]

class Header(BaseModel):
    name: str | None
    email: str | None
    phone: str | None
    linkedin: str | None
    github: str | None
    portfolio: str | None

class HeaderList(BaseModel):
    headers: list[Header]

class Summary(BaseModel):
    summary: str

class SummaryList(BaseModel):
    summary: list[Summary]