from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from publications.managers import PublicationManager
from publications.validators import validate_photo_or_video


# TODO: move these mixins to a separate file
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


class Location(models.Model):
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)

    # TODO: в приложении map добавить модели country и city, здесь поставить ForeignKey
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=50, null=True)
    building = models.CharField(max_length=10, null=True)

    place_alias = models.CharField('Название места/заведения', max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Publication(AuthorMixin, DatetimeCreatedMixin, VisibleMixin):
    text = models.TextField('Текст')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация')

    objects = PublicationManager()

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class Attachment(DatetimeCreatedMixin, AuthorMixin):
    class AttachmentType(models.TextChoices):
        PHOTO = "Photo", _("Фото")
        VIDEO = "Video", _("Видео")

    file = models.FileField('Приложение', upload_to='attachments/', validators=[validate_photo_or_video])
    file_type = models.CharField('Тип файла', choices=AttachmentType.choices, max_length=10)

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
