from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"

    class Config:
        env_file = ".env"


settings = Settings()

# Debug
print(f"SECRET_KEY: {settings.SECRET_KEY}")
print(f"DATABASE_URL: {settings.DATABASE_URL}")
