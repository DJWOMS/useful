from typing import List, Optional, Generic, TypeVar, Type

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.db.base import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def exists(self, db: Session, **kwargs):
        return db.query(
            db.query(self.model.id).filter_by(**kwargs).exists()
        ).scalar()

    def get_object_or_404(self, db: Session, id: int) -> Optional[ModelType]:
        pass

    def get(self, db: Session, **kwargs) -> Optional[ModelType]:
        return db.query(self.model).filter_by(**kwargs).first()

    def all(self, db: Session, *args, skip=0, limit=100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def filter(self, db: Session, *args, **kwargs) -> List[ModelType]:
        return db.query(self.model).filter_by(**kwargs)

    def create(self, db: Session, *args, schema: CreateSchemaType, **kwargs) -> ModelType:
        obj_in_data = jsonable_encoder(schema)
        db_obj = self.model(**obj_in_data, **kwargs)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *args, model: ModelType, schema: UpdateSchemaType) -> ModelType:
        obj_data = jsonable_encoder(model)
        update_data = schema.dict(skip_defaults=True)
        for field in obj_data:
            if field in update_data:
                setattr(model, field, update_data[field])
        db.add(model)
        db.commit()
        db.refresh(model)
        return model

    def remove(self, db: Session, *args, **kwargs) -> ModelType:
        obj = self.get(db, **kwargs)
        db.delete(obj)
        db.commit()
        return obj
