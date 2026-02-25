from app.db.database import engine, Base
from app.schemas.schema import create_schema
def db_init():
      create_schema("auth_schema")
      Base.metadata.create_all(bind=engine)