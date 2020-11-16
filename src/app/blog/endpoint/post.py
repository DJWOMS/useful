from typing import List, Optional

from fastapi import APIRouter, Depends
from .. import schemas, service
from ...auth.permissions import get_superuser
from ...user import models

post_router = APIRouter()


@post_router.post('/', response_model=schemas.GetPost)
async def create_post(schema: schemas.CreatePost):
    return await service.post_s.create(schema, author_id=2)


@post_router.get('/', response_model=List[schemas.GetPost])
async def get_all_post():
    return await service.post_s.all()


@post_router.get('/', response_model=List[schemas.GetPost])
async def filter_post(category: str, tag: str = 'one', skip: int = 0, limit: int = 10):
    return await service.post_s.filter(category=category, tag=tag, skip=skip, limit=limit)


@post_router.get('/{pk}', response_model=schemas.GetPost)
async def get_single_post(pk: int):
    return await service.post_s.get(id=pk)


@post_router.put('/{pk}', response_model=schemas.GetPost)
async def update_post(pk: int, schema: schemas.CreatePost):
    return await service.post_s.update(schema, id=pk)


@post_router.delete('/{pk}', status_code=204)
async def delete_post(pk: int):
    return await service.post_s.delete(id=pk)
