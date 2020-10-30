from typing import TypeVar, Type, Optional

from fastapi import HTTPException
from pydantic import BaseModel
from tortoise import models


ModelType = TypeVar("ModelType", bound=models.Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)


class BaseService:
    model: Type[ModelType]
    create_schema: CreateSchemaType
    update_schema: UpdateSchemaType
    get_schema: GetSchemaType

    # def __init__(self, model: Type[ModelType]):
    #     self.model = model

    async def create(self, schema, **kwargs) -> Optional[CreateSchemaType]:
        obj = await self.model.create(**schema.dict(exclude_unset=True), **kwargs)
        return await self.get_schema.from_tortoise_orm(obj)

    async def update(self, schema, **kwargs) -> Optional[UpdateSchemaType]:
        await self.model.filter(**kwargs).update(**schema.dict(exclude_unset=True))
        return await self.get_schema.from_queryset_single(self.model.get(**kwargs))

    async def all(self):
        return await self.get_schema.from_queryset(self.model.all())

    async def get(self, **kwargs):
        return await self.get_schema.from_queryset_single(self.model.get(**kwargs))

    async def get_obj(self, **kwargs):
        return await self.model.get_or_none(**kwargs)

    async def delete(self, **kwargs):
        obj = await self.model.filter(**kwargs).delete()
        if not obj:
            raise HTTPException(status_code=404, detail='Object does not exist')


