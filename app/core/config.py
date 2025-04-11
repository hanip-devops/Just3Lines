from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    """애플리케이션 설정"""
    APP_NAME: str = "Just3Lines"
    APP_VERSION: str = "1.0.0"
    OPENAI_API_KEY: str = ""
    
    model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_settings() -> Settings:
    """설정 객체를 반환합니다."""
    return Settings() 