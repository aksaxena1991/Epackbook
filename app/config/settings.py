from pydantic_settings import BaseSettings
from os import getenv
from dotenv import load_dotenv
load_dotenv()
class DbSettings(BaseSettings):
    DB_HOST: str = getenv("DB_HOST", "localhost")
    DB_PORT: int = int(getenv("DB_PORT", 5432))
    DB_NAME: str = getenv("POSTGRES_DB")
    DB_USER: str = getenv("POSTGRES_USER")
    DB_PASSWORD: str = getenv("POSTGRES_PASSWORD")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://"
            f"{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"
        extra = "ignore"

db_settings = DbSettings()