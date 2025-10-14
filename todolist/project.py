from dotenv import load_dotenv
import os

load_dotenv()
MAX_NUMBER_OF_PROJECT = int(os.getenv("MAX_NUMBER_OF_PROJECT", 5))

class Project:
    def __init__(self, name: str, description: str):
        if len(name) > 30:
            raise ValueError("Name of projects cannot be more than 30 characters")
        if len(description) > 150:
            raise ValueError("Description cannot be more than 150 characters")
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Project: {self.name}>"

class ProjectManager:
    def __init__(self):
        self.projects = []

    def create_project(self, name: str, description: str):
        if len(self.projects) >= MAX_NUMBER_OF_PROJECT:
            raise Exception("Number of projects out of range")
        if any(p.name == name for p in self.projects):
            raise Exception("There is a project with this name")
        project = Project(name, description)
        self.projects.append(project)
        return project

    def list_projects(self):
        return self.projects
