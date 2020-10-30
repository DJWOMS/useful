from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from src.config import settings
from src.app import routers


app = FastAPI(
    title="Useful",
    description="Author - DJWOMS",
    version="0.2.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)


app.include_router(routers.api_router, prefix=settings.API_V1_STR)


register_tortoise(
    app,
    db_url=settings.DATABASE_URI,
    modules={"models": settings.APPS_MODELS},
    generate_schemas=False,
    add_exception_handlers=True,
)



#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=80, debug=True)
