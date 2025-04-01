from pydantic_settings import BaseSettings, SettingsConfigDict


class MyConfig(BaseSettings):
    my_value: str
    connection_string: str
    max_user: int = 1000
    max_user2: int = 1000
    max_salary: float

    model_config = SettingsConfigDict(env_file="../.env")
