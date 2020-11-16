from typing import Optional

from src.app.base.service_base import BaseService
from src.app.blog import models, schemas


class BlogCategoryService(BaseService):
    model = models.BlogCategory
    create_schema = schemas.CreateCategory
    get_schema = schemas.GetCategory


class TagService(BaseService):
    model = models.Tag
    create_schema = schemas.CreateTag
    get_schema = schemas.GetTag


class PostService(BaseService):
    model = models.Post
    create_schema = schemas.CreatePost
    get_schema = schemas.GetPost

    async def filter(self, **kwargs) -> Optional[get_schema]:
        category, tag, skip, limit = kwargs
        return await self.get_schema.from_queryset(
            self.model.filter(category__name=category, tag__in=tag).offset(skip).limit(limit)
        )


category_s = BlogCategoryService()
tag_s = TagService()
post_s = PostService()
