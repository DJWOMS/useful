from datetime import datetime
from typing import List
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel, PydanticListModel
from . import models


class CreateCategory(PydanticModel):
    name: str
    parent_id: int = None


class GetCategory(PydanticListModel):
    id: int
    name: str
    # children: List[int] = None


class Project(PydanticModel):
    name: str
    description: str
    create_date: datetime


class GetCategoryProject(PydanticModel):
    id: int
    name: str
    projects: List[Project]

    class Config:
        orm_mode = True

# GetCategory = pydantic_model_creator(models.Category, name='get_category')


class CreateToolkit(PydanticModel):
    name: str
    parent_id: int = None


GetToolkit = pydantic_model_creator(models.Toolkit, name='get_toolkit')


class CreateProject(PydanticModel):
    name: str
    description: str
    category_id: int
    toolkit_id: int
    user_id: int


# GetProject = pydantic_model_creator(models.Project, name='get_project')

class Category(PydanticModel):
    id: int
    name: str

    # class Config:
    #     orm_mode = True


class GetProject(PydanticModel):
    name: str
    description: str
    create_date: datetime
    category: Category

    # class Config:
    #     orm_mode = True

    # user = fields.ForeignKeyField('models.User', related_name="projects")
    # toolkit = fields.ForeignKeyField('models.Toolkit', related_name="projects")
    # team = fields.ManyToManyField('models.User', related_name='team_projects')


class CreateTask(PydanticModel):
    description: str
    start_date: datetime
    end_date: datetime
    project_id: int
    worker_id: int = None

    class Config:
        schema_extra = {
            "example": {
                "description": "string",
                "start_date": "2020-10-18 15:26:17",
                "end_date": "2020-10-18 15:26:17",
                "project_id": 0,
                "worker_id": 0,
            }
        }


GetTask = pydantic_model_creator(models.Task, name='get_task')


class CreateCommentTask(PydanticModel):
    user_id: int
    task_id: int
    message: str


GetCommentTask = pydantic_model_creator(models.CommentTask, name='get_comment_task')
