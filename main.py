import uvicorn
from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.app import routers
from src.db.session import SessionLocal


app = FastAPI(
    title="Useful",
    description="Author - DJWOMS",
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(routers.api_router, prefix=settings.API_V1_STR)

#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=80, debug=True)
