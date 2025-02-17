from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config.config import db_config
import psycopg2
import asyncpg

DATABASE_URL = f"postgresql+asyncpg://{db_config.username}:{db_config.password.get_secret_value()}@{db_config.host}:{db_config.port}/UserYDB"

user_engine = create_async_engine(DATABASE_URL)

async_session = sessionmaker(class_=AsyncSession, bind=user_engine)


class UserBASE(DeclarativeBase):
    __abstract__ = True
    pass


        