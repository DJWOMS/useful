from fastapi import APIRouter
from .. import schemas, service


task_router = APIRouter()


@task_router.post('/', response_model=schemas.GetTask)
async def create_task(schema: schemas.CreateCategory):
    return await service.task_s.create(schema)


@task_router.post('/comment', response_model=schemas.GetCommentTask)
async def create_comment_task(schema: schemas.CreateCommentTask):
    return await service.comment_task_s.create(schema)
