from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class Auth(BaseModel):
    email:EmailStr
    password:str = Field(min_length=8)
    is_active:bool = False
    mobile:str = Field(min_length=10)
    timestamp: datetime
