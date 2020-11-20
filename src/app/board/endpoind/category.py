from typing import List

from fastapi import APIRouter, Depends
from .. import schemas, service, models
from ...auth.permissions import get_superuser


category_router = APIRouter()


@category_router.post('/', response_model=schemas.GetCategory)
async def create_category(
        schema: schemas.CreateCategory, user: models.User = Depends(get_superuser)
):
    return await service.category_s.create(schema)


@category_router.get('/', response_model=List[schemas.GetCategory])
async def get_category():
    return await service.category_s.filter(parent_id__isnull=True)


@category_router.put('/{pk}', response_model=schemas.GetCategory)
async def update_category(
       pk: int, schema: schemas.CreateCategory, user: models.User = Depends(get_superuser)
):
    return await service.category_s.update(schema, id=pk)


@category_router.delete('/{pk}', status_code=204)
async def delete_category(pk: int, user: models.User = Depends(get_superuser)):
    return await service.category_s.delete(id=pk)
