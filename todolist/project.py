from todolist.task import Task
import config

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
        print(f"Deleted '{name}'") 

    
    def list_projects(self):
        return self.projects
    

    def add_task(self, project_name: str, title: str, description: str, status: str = "todo"):
            project = next((p for p in self.projects if p.name == project_name), None)
            if not project:
                raise Exception(f"There is no '{project_name}'")

            tasks_for_project = self.tasks.get(project_name, [])
            if len(tasks_for_project) >= config.MAX_NUMBER_OF_TASK:
                raise Exception("Tasks are out of bound")

            new_task = Task(title, description, status)
            tasks_for_project.append(new_task)
            self.tasks[project_name] = tasks_for_project 

            return new_task
    