from sqlalchemy.orm import Session
from ..models.sqlalchemy_project import Project as DBProject
from ..models.project import Project

class SQLAlchemyProjectRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, project: Project):
        db_project = DBProject(
            id=project.id,
            name=project.name,
            description=project.description
        )
        self.session.add(db_project)
        self.session.commit()

    def list(self):
        return self.session.query(DBProject).all()

    def get(self, project_id: int):
        return self.session.query(DBProject).filter_by(id=project_id).first()

    def find_by_name(self, name: str):
        return self.session.query(DBProject).filter_by(name=name).first()

    def delete(self, project_id: int):
        project = self.session.query(DBProject).filter_by(id=project_id).first()
        if project:
            self.session.delete(project)
            self.session.commit()
