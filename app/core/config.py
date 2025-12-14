from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Workflow Processing API"
    database_url: str = "sqlite:///./workflow.db"

settings = Settings()