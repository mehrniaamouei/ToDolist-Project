from ..repositories.task_repository import TaskRepository
from ..models.task import Task

class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create_task(self, task: Task):
        self.repo.add(task)

    def list_tasks(self):
        return self.repo.list()

    def get_task(self, task_id: int):
        return self.repo.get(task_id)

    def delete_task(self, task: Task):
        self.repo.delete(task.id)
