"""Application configuration using Pydantic settings."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Database
    database_url: str = "sqlite:///./toado.db"
    
    # JWT (placeholders for Phase 2)
    jwt_secret_key: str = "your-secret-key-change-in-production"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_refresh_token_expire_days: int = 7
    
    # Email (placeholders for Phase 2)
    email_enabled: bool = False
    email_from: str = "noreply@toado.app"
    
    # Rate limiting (placeholders for Phase 2)
    rate_limit_enabled: bool = False
    rate_limit_requests: int = 100
    rate_limit_period: int = 60  # seconds
    
    # Application
    app_title: str = "Toado API"
    app_description: str = "A FastAPI-based todo management backend with a playful toad theme"
    app_version: str = "1.0.0"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
