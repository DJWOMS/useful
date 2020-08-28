from tortoise import fields, models


class User(models.Model):
    """ Model user """
    username = fields.CharField(max_length=100, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100, null=True)
    date_join = fields.DatetimeField(auto_now_add=True)
    last_login = fields.DatetimeField(null=True)
    is_active = fields.BooleanField(default=False)
    is_staff = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)
    avatar = fields.CharField(max_length=100, null=True)

    # async def save(self, *args, **kwargs) -> None:
    #     print(self.password)
    #     self.password = get_password_hash(self.password)
    #     await super().create(*args, **kwargs)


class SocialAccount(models.Model):
    """ Model social accounts
    """
    account_id = fields.IntField()
    account_url = fields.CharField(max_length=500)
    account_login = fields.CharField(max_length=100)
    account_name = fields.CharField(max_length=100)
    provider = fields.CharField(max_length=100)
    user = fields.ForeignKeyField('models.User', related_name='social_accounts')


