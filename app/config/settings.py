from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class DbSettings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "epackbook"
    DB_USER: str = "admin"
    DB_PASSWORD: str = ""

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://"
            f"{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"


# 🔒 Singleton by module import (Pythonic, thread-safe)
db_settings = DbSettings()