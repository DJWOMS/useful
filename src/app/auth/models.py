from tortoise import models, fields


class Verification(models.Model):
    """ Модель для подтверждения регистрации пользователя
    """
    link = fields.UUIDField()
    user = fields.ForeignKeyField('models.User', related_name='verification')
