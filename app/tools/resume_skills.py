from langchain_core.tools import tool
from app.core.setting import settings

class ResumeSkills:

    def __init__(self, faiss):
        self.faiss = faiss

    
    def get_tool(self):
        @tool
        def resume_skills(query: str) -> str:
            """
            Retrieve skills section from the resume.
            """

            docs = self.faiss.search(
                query=query or "technical skills",
                k=settings.TOP_K_RETRIEVER,
                filter={"type": "skills"},
            )

            return "\n\n".join(doc.page_content for doc in docs)
        return resume_skills