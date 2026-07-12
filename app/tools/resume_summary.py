from langchain_core.tools import tool
from app.core.setting import settings

class ResumeSummary:

    def __init__(self, faiss):
        self.faiss = faiss
   
    def get_tool(self):
        @tool
        def resume_summary(query: str) -> str:
            """
            Retrieve summary/profile section from the resume.
            """

            docs = self.faiss.search(
                query=query or "professional summary",
                k=settings.TOP_K_RETRIEVER,
                filter={"type": "summary"},
            )

            return "\n\n".join(doc.page_content for doc in docs)
        return resume_summary