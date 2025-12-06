from dataclasses import dataclass, field
from typing import List


@dataclass
class Project:
    id: int
    name: str
    tasks: List[int] = field(default_factory=list)