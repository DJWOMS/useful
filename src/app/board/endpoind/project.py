from typing import List
from fastapi import APIRouter, Depends

from .. import schemas, service, models
from ...auth.permissions import get_user

project_router = APIRouter()


@project_router.post('/', response_model=schemas.OutProject)
async def create_project(schema: schemas.CreateProject, user: models.User = Depends(get_user)):
    return await service.project_s.create(schema, user_id=user.id)


@project_router.get('/', response_model=List[schemas.OutProject])
async def get_all_projects():
    return await service.project_s.all()


@project_router.put('/{pk}', response_model=schemas.OutProject)
async def update_project(
        pk: int, schema: schemas.CreateProject, user: models.User = Depends(get_user)
):
    return await service.project_s.update(schema, id=pk, user_id=user.id)


@project_router.delete('/{pk}', status_code=204)
async def delete_project(pk: int, user: models.User = Depends(get_user)):
    return await service.project_s.delete(id=pk, user_id=user.id)


@project_router.post('/team', response_model=schemas.CreateTeam)
async def create_team(schema: schemas.CreateTeam, user: models.User = Depends(get_user)):
    return await service.project_s.create_team(schema, user)


# @project_router.put('/team/', response_model=schemas.CreateTeam)
# async def create_team(schema: schemas.CreateTeam):
#     return await service.project_s.create_team(schema)
