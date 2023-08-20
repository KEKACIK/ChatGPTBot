from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    OPENAI_TOKEN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
