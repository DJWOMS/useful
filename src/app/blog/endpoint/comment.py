from typing import List

from fastapi import APIRouter, Depends
from .. import schemas, service
from ...auth.permissions import get_user, get_superuser
from ...user import models

comment_router = APIRouter()


@comment_router.post('/', response_model=schemas.OutComment)
async def create_comment(schema: schemas.CreateComment, user: models.User = Depends(get_user)):
    return await service.comment_s.create(schema, user_id=user.id)


@comment_router.get('/', response_model=List[schemas.CommentChildren])
async def get_all_comment(user: models.User = Depends(get_superuser)):
    return await service.comment_s.all()


@comment_router.get('/filter', response_model=List[schemas.CommentChildren])
async def filter_comment(post_id: int, skip: int = 0, limit: int = 10):
    return await service.comment_s.filter(post_id=post_id, skip=skip, limit=limit)


@comment_router.get('/{pk}', response_model=schemas.OutComment)
async def get_single_comment(pk: int):
    return await service.comment_s.get(id=pk)


@comment_router.put('/{pk}', response_model=schemas.OutComment)
async def update_comment(
        pk: int, schema: schemas.UpdateComment, user: models.User = Depends(get_user)
):
    return await service.comment_s.update(schema, id=pk, user_id=user.id)


@comment_router.delete('/{pk}', status_code=204)
async def delete_comment(pk: int):
    return await service.comment_s.delete(id=pk)
