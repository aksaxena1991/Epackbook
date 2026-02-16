from datetime import datetime
from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, UniqueConstraint


class Auth(Base):
    __tablename__ = 'auth'

    id = Column(Integer,primary_key=True, autoincrement=True)
    email = Column(String(255),nullable=False)
    password = Column(String(255),nullable=False)
    is_active = Column(Boolean,default=False)
    mobile = Column(String(255),nullable=False, index=True)
    timestamp = Column(DateTime,default=datetime.utcnow)

    __table_args__ = (UniqueConstraint( 'email',name='unique_email'),UniqueConstraint(
        'mobile',name='unique_mobile'
    ))

