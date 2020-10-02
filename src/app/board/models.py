from tortoise import fields, models


class Category(models.Model):
    """ Categories by project
    """
    name = fields.CharField(max_length=150)
    parent = fields.ForeignKeyField("models.Category", related_name="children", null=True)


class Toolkit(models.Model):
    """ Toolkit by project
    """
    name = fields.CharField(max_length=150)
    parent = fields.ForeignKeyField("models.Toolkit", related_name="children", null=True)


class Project(models.Model):
    """ Model project
    """
    name = fields.CharField(max_length=150)
    description = fields.TextField()
    create_date = fields.DatetimeField(auto_now_add=True)
    user = fields.ForeignKeyField('models.User', related_name="projects")
    category = fields.ForeignKeyField('models.Category', related_name="projects")
    toolkit = fields.ForeignKeyField('models.Toolkit', related_name="projects")
    team = fields.ManyToManyField('models.User', related_name='team_projects')


class Task(models.Model):
    """ Model task by project
    """
    description = fields.TextField()
    create_date = fields.DatetimeField(auto_now_add=True)
    start_date = fields.DatetimeField(null=True)
    end_date = fields.DatetimeField(null=True)
    project = fields.ForeignKeyField('models.Project', related_name='tasks')
    worker = fields.ForeignKeyField('models.User', related_name='tasks')


class CommentTask(models.Model):
    """ Model comment by task
    """
    user = fields.ForeignKeyField('models.User', related_name='task_comments')
    task = fields.ForeignKeyField('models.Task', related_name='comments')
    message = fields.CharField(max_length=1000)
    create_date = fields.DatetimeField(auto_now_add=True)

