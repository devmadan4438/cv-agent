from typing import Annotated, TypedDict

from langgraph.graph.message import AnyMessage, add_messages

class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    session_id: str
    rewritten_query: str | None
    in_scope: bool