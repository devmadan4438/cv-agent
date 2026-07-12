from pydantic import BaseModel

class ResumeSection(BaseModel):
    name: str
    content: str
