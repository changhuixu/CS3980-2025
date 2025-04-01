from functools import lru_cache
import os

from models.my_config import MyConfig

value = os.getenv("MY_VALUE")
print(value)


@lru_cache
def get_settings():
    return MyConfig()


setting = get_settings()
print(setting.my_value)
print(setting.connection_string)
print(setting.max_salary)
print(setting.max_user)
print(setting.max_user2)
