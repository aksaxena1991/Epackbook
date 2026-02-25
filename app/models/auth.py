from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.database import Base


class Auth(Base):
    __tablename__ = "auth"
    __table_args__ = {"schema": "auth_schema"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)