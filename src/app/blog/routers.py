from fastapi import APIRouter
from src.app.blog.endpoint import category, tag, post, comment


blog_router = APIRouter()


blog_router.include_router(category.category_router, prefix="/category", tags=["blog"])
blog_router.include_router(tag.tag_router, prefix="/tag", tags=["blog"])
blog_router.include_router(post.post_router, prefix="/post", tags=["blog"])
blog_router.include_router(comment.comment_router, prefix="/comment", tags=["blog"])
