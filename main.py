#poetry run python main.py

from todolist.project import ProjectManager

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

def main():
    manager = ProjectManager()
    show_menu()
    while True:
        
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Project name: ")
            desc = input("Project description: ")
            try:
                p = manager.create_project(name, desc)
                print(f"\nProject created: {p}")
            except Exception as e:
                print(f"\nError: {e}")

        elif choice == "2":
            manager.list_projects()

        elif choice == "3":
            name = input("Project name to delete: ")
            try:
                manager.delete_project(name)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            project = input("Project name: ")
            title = input("Task title: ")
            desc = input("Task description: ")
            status = input("Task status (todo/doing/done): ")
            deadline = input("Deadline: ")
            try:
                manager.add_task(project, title, desc, status, deadline if deadline else None)
                print("\nTask added.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            project = input("Project name: ")
            manager.list_tasks(project)

        elif choice == "6":
            project = input("Project name: ")
            title = input("Task title to edit: ")
            new_title = input("New title (leave empty to skip): ")
            new_desc = input("New description (leave empty to skip): ")
            new_status = input("New status (todo/doing/done): ")
            new_deadline = input("New deadline: ")
            manager.edit_task(project, title, new_title or None, new_desc or None, new_status or None, new_deadline)

        elif choice == "7":
            project = input("Project name: ")
            title = input("Task title to delete: ")
            try:
                manager.delete_task(project, title)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "0":
            print("Have a nice time")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
