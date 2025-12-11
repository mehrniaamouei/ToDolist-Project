from ..repositories.sqlalchemy_project_repository import SQLAlchemyProjectRepository
from typing import Optional

class ProjectService:
    def __init__(self, repo: SQLAlchemyProjectRepository):
        self.repo = repo

    def create_project(self, name: str, description: Optional[str] = None):
        return self.repo.add(name, description)

    def list_projects(self):
        return self.repo.list()

    def get_by_id(self, project_id: int):
        return self.repo.get(project_id)

    def update_project(self, project_id: int, name: str, description: Optional[str] = None):
        return self.repo.update(project_id, name, description)

    def delete_project(self, project_id: int):
        self.repo.delete(project_id)

    def find_by_name(self, name: str):
        return self.repo.find_by_name(name)
