from src.app.user.models import User
from src.lib.github_api.service import github_s
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

    async def create_project(self, schema, user: User, repo_name: str):
        # TODO check the forked project or not
        _repo = await github_s.get_repo(user.username, repo_name)
        return _repo

    async def create_team(self, schema: schemas.CreateTeam, user: User):
        # TODO I need to create invites to users for a team
        # TODO Maybe I need to create other model for a team.
        # TODO Project O2O Team or Project FK Team
        _project = await self.get_obj(id=schema.project, user=user)
        _users = await User.filter(id__in=schema.team)
        await _project.team.add(*_users)
        return schema


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
