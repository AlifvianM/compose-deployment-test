from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

@lru_cache
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    APP_NAME: str
    APP_ENV: str
    APP_VERSION: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    CORS_ALLOW_ORIGINS: str = "*"
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: str = "*"
    CORS_ALLOW_HEADERS: str = "*"

    @property
    def cors_allow_origins_list(self) -> list[str]:
        return self.CORS_ALLOW_ORIGINS.split(",") if self.CORS_ALLOW_ORIGINS else []
    
settings = Settings()