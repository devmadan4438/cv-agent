from langchain_core.messages import HumanMessage
from app.infra.llm.factory import LLMFactory
from app.prompts.rewrite_node.reqwrite_query import SYSTEM_PROMPT
from app.graph.state import AgentState


class RewriteQueryNode:

    def __init__(self):
        self.llm = LLMFactory.get_client()

    def __call__(self, state: AgentState):
            
        history = state["messages"][:-1]

        latest = state["messages"][-1]

        prompt = f"""
            Conversation:

            {history}

            Latest Question:

            {latest.content}
        """

        rewritten = self.llm.invoke(
            [
                HumanMessage(
                    content=SYSTEM_PROMPT + "\n\n" + prompt
                )
            ]
        )

        state["rewritten_query"] = rewritten.content

        state["messages"][-1] = HumanMessage(
            content=rewritten.content
        )

        return state
