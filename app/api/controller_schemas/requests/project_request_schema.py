from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProjectCreateRequest(BaseModel):
    name: str
    description: Optional[str]

class ProjectResponse(ProjectCreateRequest):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
