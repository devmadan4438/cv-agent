from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.chat import Chat
from app.services.chat_service.chat_service import ChatService
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/")
async def chat_resume(request: Chat):
    logger.info("chat started for >", request.session_id)
    
    service = ChatService()

    generator = service.start_chat(
        session_id=request.session_id,
        message=request.message,
    )

    return StreamingResponse(generator, media_type="text/plain")