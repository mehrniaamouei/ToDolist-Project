from app.db.engine import engine
from app.db.base import Base
from app.models.sqlalchemy_project import Project
from app.models.sqlalchemy_task import Task

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tables 'projects' and 'tasks' created successfully")
