from fastapi import FastAPI
from models.base import Base
from session import engine
from settings import settings

def create_tables():
    Base.metadata.create_all(engine)

def init_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    return app

app = init_application()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return {"error": None}
# @app.get("/login")
