from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.api.controller_schemas.requests.project_request_schema import ProjectCreateRequest, ProjectResponse
from app.services.project_service import ProjectService
from app.repositories.sqlalchemy_project_repository import SQLAlchemyProjectRepository
from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/projects", tags=["Projects"])

def get_project_service(db: Session = Depends(get_db)):
    repo = SQLAlchemyProjectRepository(db)
    return ProjectService(repo)

@router.post("/", response_model=ProjectResponse, status_code=201)
def create_project(project: ProjectCreateRequest, service: ProjectService = Depends(get_project_service)):
    created_project = service.create_project(project.name, project.description)
    return created_project

@router.get("/", response_model=List[ProjectResponse])
def list_projects(service: ProjectService = Depends(get_project_service)):
    return service.list_projects()

@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, project: ProjectCreateRequest, service: ProjectService = Depends(get_project_service)):
    existing = service.get_by_id(project_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Project not found")
    updated_project = service.update_project(project_id, project.name, project.description)
    return updated_project

@router.delete("/{project_id}", status_code=204)
def delete_project(project_id: int, service: ProjectService = Depends(get_project_service)):
    existing = service.get_by_id(project_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Project not found")
    service.delete_project(project_id)
    return None
