import schedule
import time
from datetime import datetime
from app.repositories.task_repository import TaskRepository
from app.repositories.project_repository import ProjectRepository
from app.services.task_service import TaskService

task_repo = TaskRepository()
project_repo = ProjectRepository()
task_service = TaskService(task_repo)

def autoclose_overdue():
    now = datetime.now().date()
    for task in task_repo.list():
        if task.status != "done" and task.deadline and task.deadline < now:
            task.status = "done"
            task.closed_at = now
            print(f"Task '{task.title}' auto-closed.")

schedule.every(15).minutes.do(autoclose_overdue)

while True:
    schedule.run_pending()
    time.sleep(1)
