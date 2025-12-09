from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.project import Project
from app.api.controller_schemas.requests.project_request_schema import ProjectCreateRequest, ProjectResponse
from app.services.project_service import ProjectService
from app.repositories.sqlalchemy_project_repository import SQLAlchemyProjectRepository
from app.db.session import SessionLocal

router = APIRouter(prefix="/projects", tags=["Projects"])

def get_project_service():
    db = SessionLocal()
    repo = SQLAlchemyProjectRepository(db)
    return ProjectService(repo)

@router.post("/", response_model=ProjectResponse, status_code=201)
def create_project(project: ProjectCreateRequest, service: ProjectService = Depends(get_project_service)):
    project_data = Project(name=project.name, description=project.description)
    service.create_project(project_data)
    return project_data

@router.get("/", response_model=List[ProjectResponse])
async def list_projects(service: ProjectService = Depends(get_project_service)):
    return service.list_projects()

@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, project: ProjectCreateRequest, service: ProjectService = Depends(get_project_service)):
    existing = service.get_by_id(project_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Project not found")
    existing.name = project.name
    existing.description = project.description
    service.update_project(existing)
    return existing

@router.delete("/{project_id}", status_code=204)
def delete_project(project_id: int, service: ProjectService = Depends(get_project_service)):
    existing = service.get_by_id(project_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Project not found")
    service.delete_project(existing)
