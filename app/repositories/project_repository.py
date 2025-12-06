from ..models.project import Project

class ProjectRepository:
    def __init__(self):
        self._projects = []
        self._current_id = 1

    def get_next_id(self):
        next_id = self._current_id
        self._current_id += 1
        return next_id

    def add(self, project: Project):
        self._projects.append(project)

    def list(self):
        return self._projects

    def get(self, project_id: int):
        return next((p for p in self._projects if p.id == project_id), None)

    def find_by_name(self, name: str):
        return next((p for p in self._projects if p.name == name), None)

    def delete(self, project_id: int):
        self._projects = [p for p in self._projects if p.id != project_id]
