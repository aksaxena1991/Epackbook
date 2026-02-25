import app.models
from fastapi import FastAPI
from app.db.db_init import db_init
from app.db.database import engine
from app.routes.health import router as health_router
app = FastAPI(title="Singleton DB Connection")

@app.on_event("startup")
def startup_event():
    db_init()

@app.on_event("shutdown")
def shutdown_event():
    engine.dispose()

app.include_router(health_router)
