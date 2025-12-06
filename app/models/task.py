from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    description: str
    status: str = "todo"
    deadline: Optional[datetime.date] = None
