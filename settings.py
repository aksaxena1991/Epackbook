import os
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = os.getenv("PROJECT_NAME")
    PROJECT_VERSION:str = os.getenv("PROJECT_VERSION")
    POSTGRES_USER:str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD:str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB:str = os.getenv("POSTGRES_DB")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT:int = int(os.getenv("POSTGRES_PORT"))
    POSTGRES_SCHEMA: str = os.getenv("POSTGRES_SCHEMA", "public")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()
