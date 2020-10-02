from fastapi import APIRouter
from .. import schemas, service


project_router = APIRouter()


@project_router.post('/', response_model=schemas.GetProject)
async def create_project(schema: schemas.CreateProject):
    return await service.project_s.create(schema)
