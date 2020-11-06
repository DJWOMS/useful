from fastapi import APIRouter
from src.app.auth.api import auth_router
from src.app.user.endpoint import users, admin
from src.app.board.endpoind import category, toolkit, project, task
# from src.app.blog.api import blog_router

api_router = APIRouter()

# api_router.include_router(blog_router, prefix="/blog", tags=["blog"])
api_router.include_router(auth_router, prefix='/auth', tags=["login"])
api_router.include_router(users.user_router, prefix='/user', tags=["user"])
api_router.include_router(category.category_router, prefix='/board/category', tags=["board"])
api_router.include_router(toolkit.toolkit_router, prefix='/board/toolkit', tags=["board"])
api_router.include_router(project.project_router, prefix='/board/project', tags=["board"])
api_router.include_router(task.task_router, prefix='/board/task', tags=["board"])

api_router.include_router(admin.admin_router, prefix='/admin/user', tags=["admin_user"])
