from fastapi import APIRouter
from .. import schemas, service


toolkit_router = APIRouter()


@toolkit_router.post('/', response_model=schemas.GetToolkit)
async def create_toolkit(schema: schemas.CreateToolkit):
    return await service.toolkit_s.create(schema)
