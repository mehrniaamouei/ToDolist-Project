from ..db.session import SessionLocal
from ..repositories.sqlalchemy_project_repository import SQLAlchemyProjectRepository
from ..repositories.sqlalchemy_task_repository import SQLAlchemyTaskRepository
from ..services.project_service import ProjectService
from ..services.task_service import TaskService
from ..models.project import Project
from ..models.task import Task
from datetime import datetime

def run_cli():
    session = SessionLocal()
    project_repo = SQLAlchemyProjectRepository(session)
    task_repo = SQLAlchemyTaskRepository(session)
    project_service = ProjectService(project_repo)
    task_service = TaskService(task_repo)

    def show_menu():
        print("\n--- ToDo List ---")
        print("1. Create project")
        print("2. List projects")
        print("3. Delete project")
        print("4. Add task to project")
        print("5. List tasks of project")
        print("6. Edit task")
        print("7. Delete task")
        print("0. Exit")
        print("Please add deadline in YYYY-MM-DD format")

    show_menu()

    while True:
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Project name: ")
            desc = input("Project description: ")
            try:
                project = Project(id=None, name=name, description=desc)
                project_service.create_project(project)
                print(f"Project created: {project.name}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            projects = project_service.list_projects()
            if not projects:
                print("No project existed")
            else:
                for idx, p in enumerate(projects, start=1):
                    print(f"{idx}. Name: {p.name}")

        elif choice == "3":
            name = input("Project name to delete: ")
            project = project_service.find_by_name(name)
            if not project:
                print("Project not found.")
            else:
                project_service.delete_project(project)
                print(f"Deleted '{name}'")

        elif choice == "4":
            project_name = input("Project name: ")
            project = project_service.find_by_name(project_name)
            if not project:
                print(f"No project found with name '{project_name}'")
                continue
            title = input("Task title: ")
            desc = input("Task description: ")
            status = input("Task status (todo/doing/done): ") or "todo"
            deadline_str = input("Deadline (YYYY-MM-DD) or leave empty: ")
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d") if deadline_str else None
            try:
                task = Task(
                    id=None,
                    project_id=project.id,
                    title=title,
                    description=desc,
                    status=status,
                    due_date=deadline,
                    completed=False,
                    created_at=datetime.utcnow()
                )
                task_service.create_task(task)
                print("Task added.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            project_name = input("Project name: ")
            project = project_service.find_by_name(project_name)
            if not project:
                print(f"No project found with name '{project_name}'")
                continue
            tasks = [t for t in task_service.list_tasks() if t.project_id == project.id]
            for idx, t in enumerate(tasks, start=1):
                deadline_str = t.due_date.strftime("%Y-%m-%d") if t.due_date else "No deadline"
                print(f"{idx}. Title: {t.title}, Description: {t.description}, Status: {t.status}, Deadline: {deadline_str}")

        elif choice == "6":
            project_name = input("Project name: ")
            project = project_service.find_by_name(project_name)
            if not project:
                print(f"No project found with name '{project_name}'")
                continue
            tasks = [t for t in task_service.list_tasks() if t.project_id == project.id]
            if not tasks:
                print("No tasks to edit.")
                continue
            for idx, t in enumerate(tasks, start=1):
                deadline_str = t.due_date.strftime("%Y-%m-%d") if t.due_date else "No deadline"
                print(f"{idx}. Title: {t.title}, Status: {t.status}, Deadline: {deadline_str}")
            task_idx = int(input("Select task number to edit: ")) - 1
            if task_idx < 0 or task_idx >= len(tasks):
                print("Invalid task number.")
                continue
            task = tasks[task_idx]
            new_title = input(f"New title (leave empty to keep '{task.title}'): ") or task.title
            new_desc = input(f"New description (leave empty to keep '{task.description}'): ") or task.description
            new_status = input(f"New status (todo/doing/done, leave empty to keep '{task.status}'): ") or task.status
            new_deadline_str = input(f"New deadline (YYYY-MM-DD, leave empty to keep '{task.due_date}'): ")
            new_deadline = datetime.strptime(new_deadline_str, "%Y-%m-%d") if new_deadline_str else task.due_date
            task.title = new_title
            task.description = new_desc
            task.status = new_status
            task.due_date = new_deadline
            task_service.create_task(task)
            print("Task updated successfully.")

        elif choice == "7":
            project_name = input("Project name: ")
            project = project_service.find_by_name(project_name)
            if not project:
                print(f"No project found with name '{project_name}'")
                continue
            tasks = [t for t in task_service.list_tasks() if t.project_id == project.id]
            if not tasks:
                print("No tasks to delete.")
                continue
            for idx, t in enumerate(tasks, start=1):
                print(f"{idx}. {t.title}")
            task_idx = int(input("Select task number to delete: ")) - 1
            if task_idx < 0 or task_idx >= len(tasks):
                print("Invalid task number.")
                continue
            task = tasks[task_idx]
            task_service.delete_task(task)
            print(f"Task '{task.title}' deleted successfully.")

        elif choice == "0":
            print("Goodbye")
            break
