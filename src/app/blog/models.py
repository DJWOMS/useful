from tortoise import models, fields, Tortoise

from src.app.user.models import User
from src.config import settings


class BlogCategory(models.Model):
    """ Class category """
    name = fields.CharField(max_length=50)
    published = fields.BooleanField(default=True)
    parent: fields.ForeignKeyNullableRelation['BlogCategory'] = fields.ForeignKeyField(
        'models.BlogCategory', on_delete=fields.CASCADE, null=True, related_name='children'
    )
    description = fields.TextField(max_length=300)
    children: fields.ReverseRelation["BlogCategory"]
    posts: fields.ReverseRelation["Post"]

    def __str__(self):
        return self.name

    class PydanticMeta:
    #     exclude_raw_fields = False
        backward_relations = False
        exclude = ('posts', 'parent')
        allow_cycles = True
        max_recursion = 3


class Tag(models.Model):
    """ Tags class """
    name = fields.CharField(max_length=50, unique=True, null=True)
    posts: fields.ManyToManyRelation['Post']

    def __str__(self):
        return self.name


class Post(models.Model):
    """ Article class """
    author: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User', related_name='posts', on_delete=fields.CASCADE
    )
    tag: fields.ManyToManyRelation["Tag"] = fields.ManyToManyField(
        'models.Tag', through='post_tag', null=True, related_name='posts'
    )
    category: fields.ForeignKeyNullableRelation[BlogCategory] = fields.ForeignKeyField(
        'models.BlogCategory', null=True, related_name='posts', on_delete=fields.SET_NULL
    )
    title = fields.CharField(max_length=500)
    mini_text = fields.TextField(max_length=5000)
    text = fields.TextField()
    create_at = fields.DatetimeField(auto_now_add=True)
    publish_at = fields.DatetimeField(auto_now=True)
    image = fields.CharField(max_length=500, null=True)
    published = fields.BooleanField(default=True)
    viewed = fields.IntField(default=0)
    description = fields.TextField(max_length=300)

    comments: fields.ReverseRelation["Comment"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ Comment class """
    user: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User', related_name="comments", on_delete=fields.CASCADE
    )
    post: fields.ForeignKeyRelation[Post] = fields.ForeignKeyField(
        'models.Post', related_name="comments", on_delete=fields.CASCADE
    )
    parent: fields.ForeignKeyNullableRelation['Comment'] = fields.ForeignKeyField(
        "models.Comment",
        on_delete=fields.SET_NULL,
        null=True,
        related_name='children'
    )
    text = fields.TextField(max_length=2000)
    create_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)
    is_published = fields.BooleanField(default=True)
    is_deleted = fields.BooleanField(default=False)

    children: fields.ReverseRelation["Comment"]

    def __str__(self):
        return "{} - {}".format(self.user, self.post)



Tortoise.init_models(["src.app.blog.models"], "models")
