from sqlalchemy import Column, DateTime, Integer, func, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base import Base


class Auth_Session(Base):
    __tablename__ = 'auth_sessions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    auth_id = Column(Integer, ForeignKey('auth.id', ondelete='CASCADE'), nullable=False)
    token = Column(String(255), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    auth = relationship("Auth", backref="auth_sessions")