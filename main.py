from todolist.project import ProjectManager

if __name__ == "__main__":
    manager = ProjectManager()
    
    try:
        p1 = manager.create_project("first project", "this is a description")
        print("Project made", p1)
        
        p2 = manager.create_project("first project", "sec rep")
    except Exception as e:
        print("error", e)
    
    print("Projects list:", manager.list_projects())
