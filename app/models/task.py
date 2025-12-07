from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    id: Optional[int] = None
    project_id: Optional[int] = None
    title: str = ""
    description: str = ""
    status: str = "todo"
    due_date: Optional[datetime] = None
    completed: bool = False      
    created_at: Optional[datetime] = None
