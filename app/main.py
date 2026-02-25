from fastapi import FastAPI
from sqlalchemy import text
from app.db.database import engine, Base
from app.models import base as _models  # noqa: F401 — registers all models with Base.metadata
from app.routes.health import router as health_router

app = FastAPI(title="Singleton DB Connection")

@app.on_event("startup")
def startup_event():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
def shutdown_event():
    engine.dispose()

app.include_router(health_router)
