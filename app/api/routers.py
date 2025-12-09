from fastapi import APIRouter, HTTPException, Depends
from typing import List
from datetime import datetime

from app.models.project import Project
from app.models.task import Task

from app.api.controller_schemas.requests.project_request_schema import ProjectCreateRequest, ProjectResponse
from app.api.controller_schemas.requests.task_request_schema import TaskCreateRequest, TaskResponse

from app.services.project_service import ProjectService
from app.services.task_service import TaskService

from app.db.session import SessionLocal
from app.repositories.sqlalchemy_project_repository import SQLAlchemyProjectRepository
from app.repositories.sqlalchemy_task_repository import SQLAlchemyTaskRepository

router = APIRouter()

def get_project_service():
    db = SessionLocal()
    repo = SQLAlchemyProjectRepository(db)
    return ProjectService(repo)

def get_task_service():
    db = SessionLocal()
    repo = SQLAlchemyTaskRepository(db)
    return TaskService(repo)

@router.post("/projects/", response_model=ProjectResponse, status_code=201)
def create_project(project: ProjectCreateRequest, service: ProjectService = Depends(get_project_service)):
    project_data = Project(name=project.name, description=project.description)
    service.create_project(project_data)
    return project_data

@router.get("/projects/", response_model=List[ProjectResponse])
def list_projects(service: ProjectService = Depends(get_project_service)):
    return service.list_projects()

@router.get("/tasks/", response_model=List[TaskResponse])
def list_tasks(service: TaskService = Depends(get_task_service)):
    return service.list_tasks()

@router.post("/tasks/", response_model=TaskResponse, status_code=201)
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
