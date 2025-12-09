from pydantic import BaseModel
from typing import Optional

class ProjectCreateRequest(BaseModel):
    name: str
    description: Optional[str]

class ProjectResponse(ProjectCreateRequest):
    id: int
    created_at: str

    class Config:
        from_attributes = True
