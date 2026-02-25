from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.database import Base


class HealthCheck(Base):
    __tablename__ = "healthcheck"
    __table_args__ = {"schema": "auth_schema"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
