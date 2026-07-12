from langchain_core.messages import HumanMessage
from app.infra.llm.factory import LLMFactory
from app.graph.state import AgentState
from app.schemas.scope import ScopeResult

class ScopeNode:

    def __init__(self):
        self.structured_llm = LLMFactory.get_client().with_structured_output(ScopeResult)

    def __call__(self, state: AgentState):

        question = state["messages"][-1].content

        prompt = f"""
            You are a classifier.

            Determine whether the user's question is about the uploaded resume.

            Return TRUE if the user is asking about:

            - Skills
            - Experience
            - Projects
            - Education
            - Certifications
            - Contact information
            - Companies
            - Technologies used
            - Responsibilities
            - Candidate summary
            - Follow-up questions referring to previous resume answers

            Return FALSE if the user asks about:

            - Programming
            - Writing code
            - Mathematics
            - General knowledge
            - Weather
            - News
            - Creating websites
            - SQL queries
            - Anything unrelated to the resume

            Question:
            {question}
"""

        result = self.structured_llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return {
            "in_scope": result.in_scope
        }