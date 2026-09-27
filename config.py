from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Student AI Backend"
    database_url: str = "sqlite:///./student.db"
    gemini_api_key: str = ""
    gemini_model: str = "gemini-3.8-flash"
    chroma_path: str = "./.chroma"
    chroma_collection: str = "students"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()