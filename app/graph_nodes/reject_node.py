from langchain_core.messages import AIMessage


class RejectNode:

    def __call__(self, state):

        return {
            "messages": [
                AIMessage(
                    content=(
                        "I'm a resume assistant. "
                        "I can answer questions only about the uploaded resume."
                    )
                )
            ]
        }