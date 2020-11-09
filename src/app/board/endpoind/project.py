from typing import List
from fastapi import APIRouter

from .. import schemas, service, models


project_router = APIRouter()


# @project_router.post('/', response_model=schemas.GetProject)
# async def create_project(schema: schemas.CreateProject):
#     return await service.project_s.create(schema)
#
#
# @project_router.get('/', response_model=List[models.GetProject])
# async def all_project():
#     query = models.Project.all()#.select_related('category')
#     # return query
#     return await models.GetProject.from_queryset(query)
#     # return await service.project_s.all()
