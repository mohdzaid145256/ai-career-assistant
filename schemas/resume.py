from datetime import datetime

from pydantic import BaseModel


class ResumeResponse(BaseModel):
    id: int
    file_name: str
    file_path: str
    file_size: int
    created_at: datetime

    class Config:
        from_attributes = True
