from typing import List

from fastapi import APIRouter, Depends
from .. import schemas, service, models
from ...auth.permissions import get_superuser


toolkit_router = APIRouter()


@toolkit_router.post('/', response_model=schemas.GetToolkit)
async def create_toolkit(
        schema: schemas.CreateToolkit, user: models.User = Depends(get_superuser)
):
    return await service.toolkit_s.create(schema)


@toolkit_router.get('/', response_model=List[schemas.GetToolkit])
async def get_toolkit():
    return await service.toolkit_s.filter(parent_id__isnull=True)


@toolkit_router.put('/{pk}', response_model=schemas.GetToolkit)
async def update_toolkit(
       pk: int, schema: schemas.CreateToolkit, user: models.User = Depends(get_superuser)
):
    return await service.toolkit_s.update(schema, id=pk)


@toolkit_router.delete('/{pk}', status_code=204)
async def delete_toolkit(pk: int, user: models.User = Depends(get_superuser)):
    return await service.toolkit_s.delete(id=pk)
