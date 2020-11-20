from fastapi import APIRouter
from src.app.auth.api import auth_router
from src.app.user.endpoint import users, admin
from src.app.board.routers import board_router
from src.app.blog.routers import blog_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=["login"])
api_router.include_router(users.user_router, prefix='/user', tags=["user"])
api_router.include_router(board_router, prefix="/board", tags=["board"])
api_router.include_router(blog_router, prefix="/blog", tags=["blog"])

api_router.include_router(admin.admin_router, prefix='/admin/user', tags=["admin_user"])
