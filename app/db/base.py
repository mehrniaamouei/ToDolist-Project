from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models.sqlalchemy_project import Project
from app.models.sqlalchemy_task import Task
