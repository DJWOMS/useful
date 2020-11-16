from tortoise.contrib.pydantic import pydantic_model_creator
from . import models


CreateCategory = pydantic_model_creator(models.BlogCategory, exclude_readonly=True)
GetCategory = pydantic_model_creator(models.BlogCategory, exclude=('parent',))


CreateTag = pydantic_model_creator(models.Tag, exclude_readonly=True)
GetTag = pydantic_model_creator(models.Tag, exclude=('posts',))

CreatePost = pydantic_model_creator(models.Post, exclude_readonly=True, exclude=('author_id',))
GetPost = pydantic_model_creator(models.Post)
