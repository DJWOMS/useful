from fastapi import APIRouter
from tortoise import Tortoise

from .. import schemas, service, models


project_router = APIRouter()


@project_router.post('/', response_model=schemas.GetProject)
async def create_project(schema: schemas.CreateProject):
    return await service.project_s.create(schema)

