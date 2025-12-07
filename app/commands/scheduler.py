from ..db.session import SessionLocal
from ..repositories.sqlalchemy_task_repository import SQLAlchemyTaskRepository
from ..services.task_service import TaskService
from datetime import datetime
import schedule
import time

def autoclose_overdue_tasks():
    db = SessionLocal()
    try:
        task_repo = SQLAlchemyTaskRepository(db)
        task_service = TaskService(task_repo)

        tasks = task_service.list_tasks()
        now = datetime.utcnow()

        count = 0
        for t in tasks:
            if t.due_date and t.due_date < now and t.status != 'done':
                t.status = 'done'
                t.closed_at = now
                count += 1

        db.commit()
        print(f"{count} overdue tasks have been closed.")
    except Exception as e:
        db.rollback()
        print(f"Error closing tasks: {e}")
    finally:
        db.close()

def run_scheduler():
    schedule.every(15).minutes.do(autoclose_overdue_tasks)
    print("Scheduler is running... Press Ctrl+C to stop")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Scheduler stopped.")
