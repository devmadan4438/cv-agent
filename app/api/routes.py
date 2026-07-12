from fastapi import APIRouter
from .v1.upload_routes import router as upload_router
from .v1.chat_route import router as chat_router

router = APIRouter()

# Register all endpoints
router.include_router(upload_router, prefix="/v1/upload")
router.include_router(chat_router, prefix="/v1/chat")