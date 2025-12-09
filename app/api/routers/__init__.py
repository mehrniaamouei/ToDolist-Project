from fastapi import APIRouter
from .project_router import router as project_router
from .task_router import router as task_router

router = APIRouter()
router.include_router(project_router)
router.include_router(task_router)
