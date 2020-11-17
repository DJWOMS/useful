from typing import Optional, List

from fastapi import HTTPException
from tortoise.query_utils import Q

from src.app.base.service_base import BaseService
from src.app.blog import models, schemas


class BlogCategoryService(BaseService):
    model = models.BlogCategory
    create_schema = schemas.CreateCategory
    update_schema = schemas.CreateCategory
    get_schema = schemas.GetCategory


class TagService(BaseService):
    model = models.Tag
    create_schema = schemas.CreateTag
    update_schema = schemas.CreateTag
    get_schema = schemas.GetTag


class PostService(BaseService):
    model = models.Post
    create_schema = schemas.CreatePost
    update_schema = schemas.CreatePost
    get_schema = schemas.GetPost

    async def create(self, schema, tags, **kwargs) -> Optional[schemas.CreatePost]:
        obj = await self.model.create(**schema.dict(exclude_unset=True), **kwargs)
        _tags = await models.Tag.filter(id__in=tags)
        await obj.tag.add(*_tags)
        return await self.get_schema.from_tortoise_orm(obj)

    async def full_filter(
            self,
            category: str = '',
            tag: Optional[List[str]] = None,
            skip: int = 0,
            limit: int = 10
    ) -> Optional[get_schema]:
        return await self.get_schema.from_queryset(
            self.model.filter(published=True) #Q(category__name=category) | Q(tag__name__in=tag))
                .offset(skip).limit(limit).distinct()
        )


class CommentService(BaseService):
    model = models.Comment
    create_schema = schemas.CreateComment
    update_schema = schemas.UpdateComment
    get_schema = schemas.GetComment

    async def filter(self, post_id: int, skip: int = 0, limit: int = 10) -> Optional[get_schema]:
        return await self.get_schema.from_queryset(
            self.model.filter(post_id=post_id, is_published=True)
                .exclude(is_deleted=True).offset(skip).limit(limit).distinct()
        )

    async def delete(self, **kwargs):
        obj = await self.model.filter(**kwargs).update(is_deleted=True)
        if not obj:
            raise HTTPException(status_code=404, detail='Object does not exist')


category_s = BlogCategoryService()
tag_s = TagService()
post_s = PostService()
comment_s = CommentService()
