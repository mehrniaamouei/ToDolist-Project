from datetime import datetime
from sqlalchemy.orm import sessionmaker
from app.db.engine import engine
from app.models.project import Project as DomainProject
from app.models.task import Task as DomainTask
from app.repositories.sqlalchemy_project_repository import SQLAlchemyProjectRepository
from app.repositories.sqlalchemy_task_repository import SQLAlchemyTaskRepository

# ساخت session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Repositoryها
project_repo = SQLAlchemyProjectRepository(session)
task_repo = SQLAlchemyTaskRepository(session)

# تست پروژه
print("=== Project Test ===")
project = DomainProject(id=1, name="Test Project", description="Sample project")
project_repo.add(project)
all_projects = project_repo.list()
print("Projects in DB:", all_projects)
found_project = project_repo.get(1)
print("Found project:", found_project.name if found_project else None)

# تست تسک
print("\n=== Task Test ===")
task = DomainTask(id=1, project_id=1, title="Test Task", description="Sample task", due_date=datetime.utcnow())
task_repo.add(task)
all_tasks = task_repo.list()
print("Tasks in DB:", all_tasks)
found_task = task_repo.get(1)
print("Found task:", found_task.title if found_task else None)

# تمیزکاری
task_repo.delete(1)
project_repo.delete(1)

print("\n✅ Test completed successfully!")
