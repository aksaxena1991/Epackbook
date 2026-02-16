from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import settings



SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"options": f"-csearch_path={settings.POSTGRES_SCHEMA}"},
)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
