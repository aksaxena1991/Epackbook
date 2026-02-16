from fastapi import FastAPI
import re
from sqlalchemy import text
from models.base import Base
from session import engine
from settings import settings
from models.auth import Auth
from models.auth_session import Auth_Session


def create_tables():
    schema = settings.POSTGRES_SCHEMA
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", schema):
        raise ValueError(f"Invalid POSTGRES_SCHEMA value: {schema}")
    with engine.begin() as connection:
        connection.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{schema}"'))
        connection.execute(text(f'SET search_path TO "{schema}"'))
        Base.metadata.create_all(bind=connection)


def init_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )

    @app.on_event("startup")
    async def startup():
        create_tables()

    return app


app = init_application()


@app.get("/")
async def root():
    return {"message": "Hello World"}
