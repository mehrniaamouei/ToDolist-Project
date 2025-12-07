from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Project:
    id: Optional[int] = None
    name: str = ""
    description: Optional[str] = None
    tasks: List[int] = field(default_factory=list)
