from sqlalchemy import Column, Integer, String, DateTime,Boolean
from datetime import datetime
from app.db.database import Base


class Auth(Base):
    __tablename__ = "auth"
    __table_args__ = {"schema": "auth_schema"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)

    provider = Column(String, default='internal', nullable=False)
    password = Column(String, nullable=False)
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
