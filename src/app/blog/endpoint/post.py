from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from .. import schemas, service
from ...auth.permissions import get_superuser
from ...user import models

post_router = APIRouter()


@post_router.post('/', response_model=schemas.OutPost)
async def create_post(
        post: schemas.CreatePost, tags: List[int], user: models.User = Depends(get_superuser)
):
    return await service.post_s.create(post, tags, author_id=user.id)


@post_router.get('/', response_model=List[schemas.OutPost])
async def get_all_post():
    return await service.post_s.filter(is_published=True)


@post_router.get('/filter', response_model=List[schemas.OutPost])
async def filter_post(
        category: str = '', tag: Optional[List[str]] = Query(None), skip: int = 0, limit: int = 10
):
    return await service.post_s.full_filter(category=category, tag=tag, skip=skip, limit=limit)


@post_router.get('/{pk}', response_model=schemas.OutPost)
async def get_single_post(pk: int):
    return await service.post_s.get(id=pk)


@post_router.put('/{pk}', response_model=schemas.OutPost)
async def update_post(
        pk: int, schema: schemas.CreatePost, user: models.User = Depends(get_superuser)
):
    return await service.post_s.update(schema, id=pk, author_id=user.id)


@post_router.delete('/{pk}', status_code=204)
async def delete_post(pk: int, user: models.User = Depends(get_superuser)):
    return await service.post_s.delete(id=pk, author_id=user.id)
