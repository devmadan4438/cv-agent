from langchain_core.tools import tool
from app.core.setting import settings

class ResumeProject:

    def __init__(self, faiss):
        self.faiss = faiss

    def get_tool(self):

        @tool
        def resume_project(query: str) -> str:
            """Retrieve projects section from the resume."""

            docs = self.faiss.search(
                query=query or "projects",
                k=settings.TOP_K_RETRIEVER,
                filter={"type": "project"},
            )

            return "\n\n".join(doc.page_content for doc in docs)
        
        return resume_project