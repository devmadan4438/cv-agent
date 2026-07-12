from pathlib import Path
from datetime import datetime
from app.core.config import CHAT_DIR

class ChatLog:

    def __init__(self, file_path: str = f"{CHAT_DIR}/output.txt"):
        self.file_path = Path(file_path)

    def log_user(self, session_id: str, message: str):
        self._write(
            f"[{self._timestamp()}] [{session_id}] [USER]\n"
            f"{message}\n\n"
        )

    def log_agent(self, session_id: str, message: str):
        self._write(
            f"[{self._timestamp()}] [{session_id}] [AGENT]\n"
            f"{message}\n\n"
        )

    def _write(self, text: str):
        with self.file_path.open("a", encoding="utf-8") as f:
            f.write(text)

    def _timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")