from ..models.project import Project
from ..models.task import Task
from ..repositories.project_repository import ProjectRepository
from ..repositories.task_repository import TaskRepository
from ..services.project_service import ProjectService
from ..services.task_service import TaskService

def run_cli():
    project_repo = ProjectRepository()
    task_repo = TaskRepository()
    
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
                project = Project(id=project_repo.get_next_id(), name=name, tasks=[])
                project_service.create_project(project)
                print(f"\nProject created: {project}")
            except Exception as e:
                print(f"\nError: {e}")

        elif choice == "2":
            projects = project_service.list_projects()
            if not projects:
                print("No project existed")
            else:
                print("Projects list")
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
            deadline = input("Deadline: ") or None
            try:
                task = Task(id=len(task_repo.list())+1, title=title, description=desc, status=status, deadline=deadline)
                task_service.create_task(task)
                project.tasks.append(task.id)
                print("\nTask added.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            project_name = input("Project name: ")
            project = project_service.find_by_name(project_name)
            if not project:
                print(f"No project found with name '{project_name}'")
                continue
            tasks = [t for t in task_service.list_tasks() if t.id in project.tasks]
            if not tasks:
                print("No tasks found for this project.")
            else:
                for idx, t in enumerate(tasks, start=1):
                    deadline_str = t.deadline if t.deadline else "No deadline"
                    print(f"{idx}. Title: {t.title}, Description: {t.description}, Status: {t.status}, Deadline: {deadline_str}")

        elif choice == "6":
            project_name = input("Project name: ")
            project = project_service.find_by_name(project_name)
            if not project:
                print(f"No project found with name '{project_name}'")
                continue
            task_title = input("Task title to edit: ")
            task = next((t for t in task_service.list_tasks() if t.id in project.tasks and t.title == task_title), None)
            if not task:
                print("Task not found.")
                continue
            new_title = input("New title (leave empty to skip): ") or task.title
            new_desc = input("New description (leave empty to skip): ") or task.description
            new_status = input("New status (todo/doing/done, leave empty to skip): ") or task.status
            new_deadline = input("New deadline (leave empty to skip): ") or task.deadline
            task.title = new_title
            task.description = new_desc
            task.status = new_status
            task.deadline = new_deadline
            print(f"Task '{task_title}' updated successfully.")

        elif choice == "7":
            project_name = input("Project name: ")
            project = project_service.find_by_name(project_name)
            if not project:
                print(f"No project found with name '{project_name}'")
                continue
            task_title = input("Task title to delete: ")
            task = next((t for t in task_service.list_tasks() if t.id in project.tasks and t.title == task_title), None)
            if not task:
                print("Task not found.")
            else:
                project.tasks.remove(task.id)
                task_service.delete_task(task)
                print(f"Task '{task_title}' deleted successfully.")

        elif choice == "0":
            print("Have a nice time")
            break

        else:
            print("Invalid choice.")
