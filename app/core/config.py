from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "VIAAS CONNECT Backend"
    API_V1_STR: str = "/api"
    SQLALCHEMY_DATABASE_URI: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480  # 8 hours

    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-3-pro-preview"

    EMAIL_FROM: str
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str

    TWILIO_ACCOUNT_SID: str | None = None
    TWILIO_AUTH_TOKEN: str | None = None
    TWILIO_FROM_NUMBER: str | None = None

    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"


settings = Settings()
