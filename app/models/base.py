from sqlalchemy import Column, Integer, String
from datetime import datetime
from app.db.database import Base
class HealthCheck(Base):
    __tablename__ = "healthcheck"
    id = Column(Integer, primary_key=True)
    status = Column(String,nullable=False)
    created_at = Column(datetime.now(tz=None),nullable=False)
    updated_at = Column(datetime.now(tz=None),nullable=False)
