# app/api/controller_schemas/requests/task_request_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreateRequest(BaseModel):
    project_id: int
    title: str
    description: Optional[str] = None
    status: str = "todo"
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    project_id: int
    title: str
    description: Optional[str] = None
    status: str
    due_date: Optional[datetime]
    created_at: datetime
    completed: bool

    class Config:
        orm_mode = True
