from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel
from . import models


GetCategory = pydantic_model_creator(models.Category, name='get_category')
CreateCategory = pydantic_model_creator(
    models.Category, name='create_category', exclude_readonly=True, include=('parent_id', 'name')
)

GetToolkit = pydantic_model_creator(models.Toolkit, name='get_toolkit')
CreateToolkit = pydantic_model_creator(
    models.Toolkit, name='create_toolkit', exclude_readonly=True
)


class CreateProject(PydanticModel):
    name: str
    description: str
    category_id: int
    user_id: int
    toolkit_id: int


GetProject = pydantic_model_creator(models.Project, name='get_project')
# CreateProject = pydantic_model_creator(
#     models.Project, name='create_project', exclude_readonly=True,
# )


GetTask = pydantic_model_creator(models.Task, name='get_task')
CreateTask = pydantic_model_creator(
    models.Task, name='create_task', exclude_readonly=True
)


GetCommentTask = pydantic_model_creator(models.CommentTask, name='get_comment_task')
CreateCommentTask = pydantic_model_creator(
    models.CommentTask, name='create_comment_task', exclude_readonly=True
)
