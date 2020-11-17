from datetime import datetime
from typing import List

from pydantic.main import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel
from . import models
from ..user.schemas import UserPublic

CreateCategory = pydantic_model_creator(models.BlogCategory, exclude_readonly=True)
GetCategory = pydantic_model_creator(models.BlogCategory, exclude=('parent',))


class CategoryForPost(BaseModel):
    id: int
    name: str


CreateTag = pydantic_model_creator(models.Tag, exclude_readonly=True, exclude=('posts',))
GetTag = pydantic_model_creator(models.Tag, exclude=('posts',))


CreatePost = pydantic_model_creator(
    models.Post,
    exclude_readonly=True,
    exclude=('author_id',)
)

GetPost = pydantic_model_creator(models.Post, exclude=('published', 'category__children'))


class OutPost(PydanticModel):
    id: int
    author: UserPublic
    tag: List[GetTag] = []
    category: CategoryForPost
    title: str
    mini_text: str
    text: str
    create_at: datetime
    publish_at: datetime
    image: str = None
    viewed: int
    description: str


CreateComment = pydantic_model_creator(
    models.Comment,
    exclude_readonly=True,
    exclude=('user_id', 'is_published', 'is_deleted', 'posts')
)

GetComment = pydantic_model_creator(
    models.Comment,
    exclude=('post', 'parent')
)


class UpdateComment(BaseModel):
    text: str


class OutComment(PydanticModel):
    id: int
    user: UserPublic
    post_id: int
    text: str
    create_at: datetime
    update_at: datetime


class CommentChildren(OutComment):
    children: List[OutComment]
