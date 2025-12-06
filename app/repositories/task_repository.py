from typing import Optional, List
from ..models.task import Task

class TaskRepository:
    def __init__(self):
        self._tasks: List[Task] = []

    def add(self, task: Task):
        self._tasks.append(task)

    def list(self):
        return self._tasks

    def get(self, task_id: int) -> Optional[Task]:
        return next((t for t in self._tasks if t.id == task_id), None)

    def delete(self, task_id: int):
        self._tasks = [t for t in self._tasks if t.id != task_id]
