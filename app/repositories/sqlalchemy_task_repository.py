from sqlalchemy.orm import Session
from typing import Optional
from ..models.sqlalchemy_task import Task as DBTask
from ..models.task import Task
from datetime import datetime

class SQLAlchemyTaskRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, task: Task):
        db_task = DBTask(
            id=task.id,
            project_id=task.project_id,
            title=task.title,
            description=task.description,
            status=task.status,
            due_date=task.due_date,
            completed=task.completed,
            created_at=task.created_at or datetime.utcnow()
        )
        self.session.add(db_task)
        self.session.commit()

    def list(self):
        return self.session.query(DBTask).all()

    def get(self, task_id: int) -> Optional[Task]:
        return self.session.query(DBTask).filter_by(id=task_id).first()

    def delete(self, task_id: int):
        task = self.session.query(DBTask).filter_by(id=task_id).first()
        if task:
            self.session.delete(task)
            self.session.commit()
