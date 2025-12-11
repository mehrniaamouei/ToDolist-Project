from sqlalchemy.orm import Session
from typing import Optional
from ..models.sqlalchemy_project import Project as DBProject

class SQLAlchemyProjectRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, name: str, description: Optional[str] = None):
        db_project = DBProject(
            name=name,
            description=description
        )
        self.session.add(db_project)
        self.session.commit()
        self.session.refresh(db_project)
        return db_project

    def list(self):
        return self.session.query(DBProject).all()

    def get(self, project_id: int):
        return self.session.query(DBProject).filter_by(id=project_id).first()

    def find_by_name(self, name: str):
        return self.session.query(DBProject).filter_by(name=name).first()

    def update(self, project_id: int, name: str, description: Optional[str] = None):
        project = self.session.query(DBProject).filter_by(id=project_id).first()
        if project:
            project.name = name
            project.description = description
            self.session.commit()
            self.session.refresh(project)
        return project

    def delete(self, project_id: int):
        project = self.session.query(DBProject).filter_by(id=project_id).first()
        if project:
            self.session.delete(project)
            self.session.commit()
