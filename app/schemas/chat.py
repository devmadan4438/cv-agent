from pydantic import BaseModel

class Chat(BaseModel):
    message: int
    session_id: str
