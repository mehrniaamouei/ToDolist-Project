#poetry run python -m app.main
#docker start todolist-db
#docker exec -it todolist-db psql -U mehr -d todolist
#poetry run uvicorn app.main:app --reload



from fastapi import FastAPI
from app.api.routers import router

app = FastAPI(
    title="ToDoList API",
    description="API for managing Projects and Tasks",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

