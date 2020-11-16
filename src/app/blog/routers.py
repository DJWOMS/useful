from fastapi import APIRouter
from src.app.blog.endpoint import category


blog_router = APIRouter()


blog_router.include_router(category.category_router, prefix="/category", tags=["blog"])

