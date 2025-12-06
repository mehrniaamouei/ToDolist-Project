from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from app.db.engine import engine

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Table 'projects' created successfully!")
