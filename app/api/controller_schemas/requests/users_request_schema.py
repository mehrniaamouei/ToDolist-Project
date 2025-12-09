
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProjectCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
