from datetime import datetime

from pydantic import BaseModel


class JobResponse(BaseModel):
    id: int
    title: str
    prompt: str
    model_output: str
    created_at: datetime

    model_config = {"from_attributes": True}
