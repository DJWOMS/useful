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


category_s = BlogCategoryService()
tag_s = TagService()
