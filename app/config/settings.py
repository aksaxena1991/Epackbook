from pydantic_settings import BaseSettings

class DbSettings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "epackbook"
    DB_USER: str = "admin"
    DB_PASSWORD: str = 1689923100

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