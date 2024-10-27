from datetime import timedelta, datetime

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "SocialNetwork"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_EXPIRATION_TIME: timedelta = timedelta(minutes=480)

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file="src/.env")

settings = Settings()