from todolist.task import Task
import config
from datetime import datetime


class Project:
    def __init__(self, name: str, description: str):
        if len(name) > 30:
            raise ValueError("Name of projects cannot be more than 30 characters.")
        if len(description) > 150:
            raise ValueError("Description cannot be more than 150 characters.")
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<<Project: {self.name}>>"

class ProjectManager:
    def __init__(self):
        self.projects = []
        self.tasks = {}

    def _get_project_by_name(self, project_name: str):
        project = next((p for p in self.projects if p.name == project_name), None)
        if not project:
            raise Exception(f"No project found with the name '{project_name}'")
        return project

    def create_project(self, name: str, description: str):
        if len(self.projects) >= config.MAX_NUMBER_OF_PROJECT:
            raise Exception("Number of projects out of range.")
        if any(p.name == name for p in self.projects):
            raise Exception("There is a project with this name.")
        project = Project(name, description)
        self.projects.append(project)
        return project
        
    def edit_project(self, old_name: str, new_name: str, new_description: str):
        project = next((p for p in self.projects if p.name == old_name), None)
        if not project:
            raise Exception(f"No project with '{old_name}' name was found.")
        if len(new_name) > 30:
            raise ValueError("Name of projects cannot be more than 30 characters.")
        if len(new_description) > 150:
            raise ValueError("Description cannot be more than 150 characters.")
        
        if any(p.name == new_name and p != project for p in self.projects):
            raise Exception("Choose another name.")

        project.name = new_name
        project.description = new_description
        return project

    def delete_project(self, name: str):
        project = next((p for p in self.projects if p.name == name), None)
        if not project:
            raise Exception("Project not found.")
        
        self.projects.remove(project)
        if name in self.tasks:
            del self.tasks[name]
        print(f"Deleted '{name}'") 

    
    def list_projects(self):
        if not self.projects:
            print("No project existed")
            return []

        print("Projects list")
        for idx, project in enumerate(self.projects, start=1):
            print(f"{idx}. Name: {project.name} | Description: {project.description}")

        return self.projects
    


    def add_task(self, project_name: str, title: str, description: str, status: str = "todo", deadline: str = None):
        self._get_project_by_name(project_name)

        if not status: 
            status = "todo"

        tasks_for_project = self.tasks.get(project_name, [])
        if len(tasks_for_project) >= config.MAX_NUMBER_OF_TASK:
            raise Exception("Tasks are out of bound")

        new_task = Task(title, description, status, deadline)
        tasks_for_project.append(new_task)
        self.tasks[project_name] = tasks_for_project 

        return new_task

    def change_task_status(self, project_name: str, task_title: str, new_status: str):
        self._get_project_by_name(project_name)

        if new_status not in ["todo", "doing", "done"]:
            raise ValueError("Status MUST be one of this folowings: todo, doing, done")

        tasks_for_project = self.tasks.get(project_name, [])
        task = next((t for t in tasks_for_project if t.title == task_title), None)
        if not task:
            raise Exception(f"No task found with the title '{task_title}' in project '{project_name}'")

        task.status = new_status
        return task
        
    def delete_task(self, project_name: str, task_title: str):
        self._get_project_by_name(project_name)

        tasks_for_project = self.tasks.get(project_name, [])

        task_to_delete = next((t for t in tasks_for_project if t.title == task_title), None)
        if not task_to_delete:
            raise Exception(f"No task found with the title '{task_title}' in project '{project_name}'")

        tasks_for_project.remove(task_to_delete)
        print(f"Task '{task_title}' deleted successfully from project '{project_name}'.")

    def edit_task(self, project_name: str, task_title: str, new_title: str = None,
                  new_description: str = None, new_status: str = None, new_deadline: str = None):
        self._get_project_by_name(project_name)

        tasks_for_project = self.tasks.get(project_name, [])
        task = next((t for t in tasks_for_project if t.title == task_title), None)
        if not task:
            raise Exception(f"No task found with the title '{task_title}' in project '{project_name}'")

        if new_title is not None:
            if len(new_title) > 30:
                raise ValueError("Title cannot be more than 30 characters.")
            task.title = new_title

        if new_description is not None:
            if len(new_description) > 150:
                raise ValueError("Description cannot be more than 150 characters.")
            task.description = new_description

        if new_status is not None:
            if new_status not in ["todo", "doing", "done"]:
                raise ValueError("Status MUST be one of: todo, doing, done")
            task.status = new_status

        if new_deadline is not None:
            if new_deadline == "":
                task.deadline = None
            else:
                try:
                    parsed_date = datetime.strptime(new_deadline, "%Y-%m-%d")
                except ValueError:
                    raise ValueError("Deadline must be in the format YYYY-MM-DD.")
                if parsed_date.date() < datetime.now().date():
                    raise ValueError("Deadline cannot be in the past.")
                task.deadline = parsed_date.date()

        print(f"Task '{task_title}' in project '{project_name}' was successfully edited.")
        return task 

    def list_tasks(self, project_name: str):
        project = next((p for p in self.projects if p.name == project_name), None)
        if not project:
            print(f"No project found with the name '{project_name}'.")
            return []

        tasks_for_project = self.tasks.get(project_name, [])
        if not tasks_for_project:
            print(f"No tasks found for project '{project_name}'.")
            return []

        for idx, task in enumerate(tasks_for_project, start=1):
            deadline_str = task.deadline.strftime("%Y-%m-%d") if task.deadline else "No deadline"
            print(f"{idx}. Title: {task.title}, Status: {task.status}, Deadline: {deadline_str}")

        return tasks_for_project
