from ..repositories.sqlalchemy_project_repository import SQLAlchemyProjectRepository
from ..models.project import Project

class ProjectService:
    def __init__(self, repo: SQLAlchemyProjectRepository):
        self.repo = repo

    def create_project(self, project: Project):
        self.repo.add(project)

    def list_projects(self):
        return self.repo.list()

    def delete_project(self, project: Project):
        self.repo.delete(project.id)

    def find_by_name(self, name: str):
        return self.repo.find_by_name(name)
