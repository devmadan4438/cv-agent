from app.graph.state import AgentState

FOLLOWUP_WORDS = {
    "it",
    "its",
    "they",
    "them",
    "there",
    "that",
    "those",
    "this",
    "these",
    "he",
    "she",
    "his",
    "her",
    "former",
    "latter",
    "previous",
    "above",
    "same",
    "another",
    "also",
}


class QuestionRouterNode:

    def __call__(self, state:AgentState):
        messages = state["messages"]

        # First question
        if len(messages) <= 1:
            return {
                "route": "standalone"
            }

        question = messages[-1].content.lower()

        if any(word in question.split() for word in FOLLOWUP_WORDS):
            return {
                "route": "rewrite"
            }

        return {
            "route": "standalone"
        }
