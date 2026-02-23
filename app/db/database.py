from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from app.config.settings import db_settings

engine = create_engine(
    db_settings.database_url,
    pool_pre_ping=True,
)

Base = declarative_base()