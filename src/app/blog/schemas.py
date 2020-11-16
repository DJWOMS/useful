from tortoise.contrib.pydantic import pydantic_model_creator
from . import models


CreateCategory = pydantic_model_creator(models.BlogCategory, exclude_readonly=True)
GetCategory = pydantic_model_creator(models.BlogCategory, exclude=('parent',))


CreateTag = pydantic_model_creator(models.Tag, exclude_readonly=True)
GetTag = pydantic_model_creator(models.Tag, exclude=('posts',))
