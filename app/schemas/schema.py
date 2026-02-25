from sqlalchemy import text
from app.db.database import engine

def create_schema(schema_name:str):
    with engine.connect() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))
        conn.commit()