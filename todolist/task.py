class Task:
    def __init__(self, title: str, description: str, status: str = "todo"):
        if len(title) > 30:
            raise ValueError("Name of projects cannot be more than 30 characters.")
        if len(description) > 150:
            raise ValueError("Description cannot be more than 150 characters.")
        if status not in ["todo", "doing", "done"]:
            raise ValueError("Status MUST be one of this folowings: todo, doing, done")

        self.title = title
        self.description = description
        self.status = status

    def __repr__(self):
        return f"<<Task: {self.title} ({self.status})>>"
