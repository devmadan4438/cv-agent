from langchain_core.messages import  SystemMessage
from app.infra.llm.factory import LLMFactory
from app.prompts.agent_node.system_prompt import SYSTEM_PROMPT
from app.graph.state import AgentState

class AgentNode:

    def __init__(self, tools):
        self.llm = (
            LLMFactory.get_client()
            .bind_tools(tools)
        )

    def __call__(self, state: AgentState):

        messages = [
                SystemMessage(content=SYSTEM_PROMPT),
                *state["messages"]
            ]

        response = self.llm.invoke(messages)

        return {
            "messages": [response]
        }