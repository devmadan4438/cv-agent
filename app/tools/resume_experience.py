from langchain_core.tools import tool
from app.core.setting import settings

class ResumeExperience:

    def __init__(self, faiss):
        self.faiss = faiss

    
    def get_tool(self):

        @tool
        def resume_experience(query: str) -> str:
            """
            Retrieve experience section from the resume.
            """

            docs = self.faiss.search(
                query=query,
                k=settings.TOP_K_RETRIEVER,
                filter={"type": "experience"},
            )

            return "\n\n".join(doc.page_content for doc in docs)
        
        return resume_experience