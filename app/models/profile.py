from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.db.database import Base


class Profile(Base):
    __tablename__ = "profile"
    __table_args__ = {"schema": "auth_schema"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    auth_id = Column(Integer, ForeignKey("auth_schema.auth.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("auth_schema.role.id"), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)