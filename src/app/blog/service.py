from src.app.base.service_base import BaseService
from src.app.blog import models, schemas


class BlogCategoryService(BaseService):
    model = models.BlogCategory
    create_schema = schemas.CreateCategory
    query_schema = schemas.GetListCategory
    get_schema = schemas.GetCategory


category_s = BlogCategoryService()
