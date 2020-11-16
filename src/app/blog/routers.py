from fastapi import APIRouter
from src.app.blog.endpoint import category, tag


blog_router = APIRouter()


blog_router.include_router(category.category_router, prefix="/category", tags=["blog"])
blog_router.include_router(tag.tag_router, prefix="/tag", tags=["blog"])
