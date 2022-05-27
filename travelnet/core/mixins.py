from django.contrib.auth import get_user_model
from django.db import models


class DatetimeCreatedMixin(models.Model):
    datetime_created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        abstract = True


class VisibleMixin(models.Model):
    visible = models.BooleanField('Видимость', default=True)

    class Meta:
        abstract = True


class AuthorMixin(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        abstract = True

