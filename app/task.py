from datetime import datetime

class Task:
    def __init__(self, title: str, description: str, status: str = "todo", deadline: str = None):
        if len(title) > 30:
            raise ValueError("Title cannot be more than 30 characters.")
        if len(description) > 150:
            raise ValueError("Description cannot be more than 150 characters.")
        if status not in ["todo", "doing", "done"]:
            raise ValueError("Status MUST be one of the following: todo, doing, done")

        self.title = title
        self.description = description
        self.status = status
        self.deadline = None 

        if deadline:
            try:
                parsed_date = datetime.strptime(deadline, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Deadline must be in the format YYYY-MM-DD.")
            
            if parsed_date.date() < datetime.now().date():
                raise ValueError("Deadline cannot be in the past.")
            
            self.deadline = parsed_date.date()

    def __repr__(self):
        deadline_str = self.deadline.strftime("%Y-%m-%d") if self.deadline else "No deadline"
        return f"<<Task: {self.title} ({self.status}) - Deadline: {deadline_str}>>"

