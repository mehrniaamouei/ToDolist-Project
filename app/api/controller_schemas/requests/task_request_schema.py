from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreateRequest(BaseModel):
    project_id: int
    title: str
    description: Optional[str]
    status: Optional[str] = "todo"
    due_date: Optional[datetime]

class TaskResponse(TaskCreateRequest):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True
