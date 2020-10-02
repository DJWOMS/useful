from . import schemas, models
from ..base.service_base import BaseService


class CategoryService(BaseService):
    model = models.Category
    create_schema = schemas.CreateCategory
    get_schema = schemas.GetCategory


class ToolkitService(BaseService):
    model = models.Toolkit
    create_schema = schemas.CreateToolkit
    get_schema = schemas.GetToolkit


class ProjectService(BaseService):
    model = models.Project
    create_schema = schemas.CreateProject
    get_schema = schemas.GetProject


class TaskService(BaseService):
    model = models.Task
    create_schema = schemas.CreateTask
    get_schema = schemas.GetTask


class CommentTaskService(BaseService):
    model = models.CommentTask
    create_schema = schemas.CreateCommentTask
    get_schema = schemas.GetCommentTask


category_s = CategoryService()
toolkit_s = ToolkitService()
project_s = ProjectService()
task_s = TaskService()
comment_task_s = CommentTaskService()
