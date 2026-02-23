from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.session import get_db

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/db")
def get_health(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1")).scalar()
    return {"database": "up", "result": result}