from langchain_core.tools import tool
from app.core.setting import settings

class ResumeSearch:

    def __init__(self, faiss):
        self.faiss = faiss
    
    def get_tool(self):
        @tool
        def resume_search(query: str) -> str:
            """
            Search the entire resume for information relevant to the user's question.
            """
            docs = self.faiss.search(query=query, k=settings.TOP_K_RETRIEVER)
            return "\n\n".join(doc.page_content for doc in docs)
        return resume_search