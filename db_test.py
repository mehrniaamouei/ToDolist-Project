#poetry run python db_test.py

from app.db.session import SessionLocal
from app.models.project import Project

db = SessionLocal()
projects = db.query(Project).all()
for p in projects:
    print(p.name, p.description)
