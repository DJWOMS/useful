from fastapi import APIRouter
from .. import schemas, service


category_router = APIRouter()


@category_router.post('/', response_model=schemas.GetCategory)
async def create_category(schema: schemas.CreateCategory):
    return await service.category_s.create(schema)

