from typing import List

from fastapi import APIRouter, Depends
from .. import schemas, service
from ...auth.permissions import get_superuser
from ...user import models

tag_router = APIRouter()


@tag_router.post('/', response_model=schemas.GetTag)
async def create_tag(schema: schemas.CreateTag, user: models.User = Depends(get_superuser)):
    return await service.tag_s.create(schema)


@tag_router.get('/', response_model=List[schemas.GetTag])
async def get_all_tag():
    return await service.tag_s.all()


@tag_router.get('/{pk}', response_model=schemas.GetTag)
async def get_single_tag(pk: int):
    return await service.tag_s.get(id=pk)


@tag_router.put('/{pk}', response_model=schemas.GetTag)
async def update_tag(pk: int, schema: schemas.CreateTag, user: models.User = Depends(get_superuser)):
    return await service.tag_s.update(schema, id=pk)


@tag_router.delete('/{pk}', status_code=204)
async def delete_tag(pk: int, user: models.User = Depends(get_superuser)):
    return await service.tag_s.delete(id=pk)
