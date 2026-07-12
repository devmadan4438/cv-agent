from pydantic import BaseModel, Field


class ScopeResult(BaseModel):
    in_scope: bool = Field(
        description="True if the question is about the uploaded resume."
    )