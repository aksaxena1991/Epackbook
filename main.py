from fastapi import FastAPI
from models.base import Base
from session import engine
from settings import settings
from models.auth import Auth
from models.auth_session import Auth_Session


def create_tables():
    Base.metadata.create_all(bind=engine)


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