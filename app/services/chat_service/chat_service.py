from langchain_core.messages import HumanMessage
from app.services.session.session_manager import SessionManager
from .chat_log import ChatLog
import logging

chatlog = ChatLog()

logger = logging.getLogger(__name__)

class ChatService:

    def start_chat(
        self,
        session_id: str,
        message: str,
        mode: str = 'API'
    ):
        try:
            chatlog.log_user(session_id, message)

            session = SessionManager()
            graph = session.get_graph(session_id=session_id)

            config = {
                "configurable": {
                    "thread_id": session_id
                },
                "run_name": "Resume Chat",
                "metadata": { # For better tracing
                    "session_id": session_id,
                    "mode": mode,
                }
            }

            full_response  = []

            for msg, metadata in graph.stream(
                {
                    "messages": [
                        HumanMessage(content=message)
                    ],
                    "session_id": session_id,
                },
                config=config,
                stream_mode="messages",
            ):
                # Only stream responses from the final agent
                if metadata.get("langgraph_node") != "agent_node":
                    continue

                if getattr(msg, "content", None):
                    full_response.append(msg.content)
                    yield msg.content
            
            chatlog.log_agent(
                session_id,
                "".join(full_response)
            )

        except Exception as e:
            logger.exception("Chat streaming failed")
            raise