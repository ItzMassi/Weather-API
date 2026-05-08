from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    visual_crossing_api_key: str
    redis_host: str = "localhost"
    redis_port: int = 6379
    cache_expire_seconds: int = 1800

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
