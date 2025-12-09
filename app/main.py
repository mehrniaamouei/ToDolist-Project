#poetry run python -m app.main
#docker exec -it todolist-db psql -U mehr -d todolist


from fastapi import FastAPI
from app.api.routers import router

app = FastAPI(
    title="ToDoList API",
    description="API for managing Projects and Tasks",
    version="1.0.0"
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
