from fastapi import APIRouter, HTTPException, Depends
from typing import List
from datetime import datetime
from app.models.task import Task
from app.api.controller_schemas.requests.task_request_schema import TaskCreateRequest, TaskResponse
from app.services.task_service import TaskService
from app.repositories.sqlalchemy_task_repository import SQLAlchemyTaskRepository
from app.db.session import SessionLocal

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_task_service():
    db = SessionLocal()
    repo = SQLAlchemyTaskRepository(db)
    return TaskService(repo)

@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreateRequest, service: TaskService = Depends(get_task_service)):
    task_data = Task(
        project_id=task.project_id,
        title=task.title,
        description=task.description,
        status=task.status,
        due_date=task.due_date,
        completed=False,
        created_at=datetime.utcnow()
    )
    service.create_task(task_data)
    return task_data

@router.get("/", response_model=List[TaskResponse])
def list_tasks(service: TaskService = Depends(get_task_service)):
    return service.list_tasks()

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreateRequest, service: TaskService = Depends(get_task_service)):
    existing = service.get_by_id(task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    existing.title = task.title
    existing.description = task.description
    existing.status = task.status
    existing.due_date = task.due_date
    service.update_task(existing)
    return existing

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    existing = service.get_by_id(task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    service.delete_task(existing)
