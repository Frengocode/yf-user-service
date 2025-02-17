from pydantic_settings import BaseSettings
from pydantic import SecretStr
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()


class DBConfig(BaseSettings):
    username: str
    password: SecretStr
    host: str
    port: int


class RedisConifg(BaseSettings):
    host: str
    port: int


class RMQConifg(BaseSettings):
    username: str
    password: SecretStr
    host: str
    port: int


db_config = DBConfig(
    username=os.getenv("PG_USERNAME"),
    password=os.getenv("PG_PASSWORD"),
    host=os.getenv("PG_HOST"),
    port=os.getenv("PG_PORT"),
)

redis_config = RedisConifg(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"))

rmq_cli_config = RMQConifg(
    username=os.getenv("RMQ_USERNAME"),
    password=os.getenv("RMQ_PASSWORD"),
    port=os.getenv("RMQ_PORT"),
    host=os.getenv("RMQ_HOST"),
)
