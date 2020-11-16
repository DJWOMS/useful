from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from . import models


CreateCategory = pydantic_model_creator(models.BlogCategory, exclude_readonly=True)
GetCategory = pydantic_model_creator(models.BlogCategory, exclude=('parent',)) #  'posts', 'children__posts'))
GetListCategory = pydantic_queryset_creator(models.BlogCategory, exclude=('parent', 'children', 'posts'))

