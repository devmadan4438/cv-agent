from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from .state import AgentState

from app.graph_nodes.agent_node import AgentNode
from app.graph_nodes.rewrite_query_node import RewriteQueryNode
from app.graph_nodes.question_route_node import QuestionRouterNode
from app.graph_nodes.scope_node import ScopeNode
from app.graph_nodes.reject_node import RejectNode

from langgraph.prebuilt.tool_node import ToolNode

class Workflow:

    def __init__(self, tools):
        self.tools = tools
        self.builder = StateGraph(AgentState)
        self.graph_client = None

    def should_continue(self, state: AgentState) -> str:
        """
        Decide whether the agent requested a tool.
        """

        last_message = state["messages"][-1]

        if getattr(last_message, "tool_calls", None):
            return "tool_node"

        return END

    def route_question(self, state):

        return state["route"]

    def route_scope(self, state: AgentState):
        if state["in_scope"]:
            return "agent"

        return "reject"

    def build_graph(self):
        agent_node = AgentNode(self.tools)
        rewrite_query = RewriteQueryNode()
        question_router = QuestionRouterNode()


        # Nodes
        self.builder.add_node("question_router", question_router)
        self.builder.add_node("rewrite_query_node", rewrite_query)
        self.builder.add_node("agent_node", agent_node)
        self.builder.add_node("tool_node", ToolNode(self.tools))
        self.builder.add_node("scope_node", ScopeNode())
        self.builder.add_node("reject_node", RejectNode())

        # Entry
        self.builder.set_entry_point("question_router")

        # question to agent_node or reqwrite_node
        self.builder.add_conditional_edges(
            "question_router",
            self.route_question,
            {
                "standalone": "scope_node",
                "rewrite": "rewrite_query_node",
            },
        )

        # rewrite to agent
        self.builder.add_edge(
            "rewrite_query_node",
            "scope_node",
        )

        # agent to tool OR end
        self.builder.add_conditional_edges(
            "agent_node",
            self.should_continue,
            {
                "tool_node": "tool_node",
                END: END,
            },
        )

        self.builder.add_conditional_edges(
            "scope_node",
            self.route_scope,
            {
                "agent": "agent_node",
                "reject": "reject_node",
            },
        )

        # tool to agent
        self.builder.add_edge(
            "tool_node",
            "agent_node",
        )

        self.builder.add_edge(
            "reject_node",
            END,
        )

        self.graph_client = self.builder.compile(
            checkpointer=MemorySaver()
        )

    def get_graph(self):
        return self.graph_client