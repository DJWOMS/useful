from typing import List

from fastapi import APIRouter, Depends
from .. import schemas, service
from ...auth.permissions import get_superuser
from ...user import models

category_router = APIRouter()


@category_router.post('/', response_model=schemas.GetCategory)
async def create_category(schema: schemas.CreateCategory, user: models.User = Depends(get_superuser)):
    return await service.category_s.create(schema)


@category_router.get('/', response_model=List[schemas.GetCategory])
async def get_all_category():
    return await service.category_s.filter(parent_id__isnull=True)


@category_router.get('/{pk}', response_model=schemas.GetCategory)
async def get_single_category(pk: int):
    return await service.category_s.get(id=pk)
