from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

import uvicorn

from app.api.routes import router as register_routes
from app.core.logger import setup_logger

from .core.setting import settings
from .core.exceptions import (
    AppException, 
    app_exception_handler, 
    validation_exception_handler, 
    global_exception_handler
    )

app = FastAPI(title="AI Boundaryless CV Agent")

# middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Error Handlers
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

# routes
app.include_router(register_routes, prefix="/api")

def start():
    # setup logger
    setup_logger()

    # start server
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.PORT, reload=True)        
    
if __name__ == "__main__":
    start()
