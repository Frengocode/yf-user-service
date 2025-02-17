from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from services.user.router import user_router
from core.database.user import user_engine, UserBASE
from starlette.responses import Response
import time
import prometheus_client


def create_app() -> FastAPI:
    _app = FastAPI(
        title="User Service Api V1",
        description="Yandex Product User",
        version="0.1.0",
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # или укажите конкретные источники
        allow_credentials=True,
        allow_methods=["*"],  # Разрешаем все HTTP-методы
        allow_headers=["*"],  # Разрешаем все заголовки
    )

    _app.include_router(user_router)

    return _app


app = create_app()


async def create_teables():
    async with user_engine.begin() as conn:
        await conn.run_sync(UserBASE.metadata.create_all)


@app.on_event("startup")
async def on_startup():
    return await create_teables()
