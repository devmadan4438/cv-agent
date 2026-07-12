from app.core.config import VECTOR_DIR
from app.graph.workflow import Workflow
from app.services.embedding.factory import EmbeddingFactory
from app.services.vector_store.faiss import FAISSService
from app.tools.factory import ToolFactory
import logging

# logger
logger = logging.getLogger(__name__)

class SessionManager:

    _cache = {}

    @classmethod
    def get_graph(cls, session_id: str):

        if session_id in cls._cache:
            logging.info("Session picked from cache:> ", session_id)
            return cls._cache[session_id]

        embeddings  = EmbeddingFactory.get('nomic').get_embeddings()

        faiss = (
            FAISSService(embeddings)
            .load(f"{VECTOR_DIR}/{session_id}")
        )

        tools = ToolFactory(faiss).get_tools()

        workflow = Workflow(tools)
        workflow.build_graph()

        graph = workflow.get_graph()

        cls._cache[session_id] = graph

        logging.info("Session created:> ", session_id)
        return graph