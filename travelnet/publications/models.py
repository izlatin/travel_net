from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mapbox_location_field.models import LocationField

from .managers import PublicationManager
from .validators import validate_photo_or_video


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


class Publication(AuthorMixin, DatetimeCreatedMixin, VisibleMixin):
    text = models.TextField('Текст')
    location = LocationField("Расположение", map_attrs={
        "placeholder": "Выберите геопозицию на карте", "zoom": 7,
        "language": "ru",
        "center": [37.60024739728942, 55.763870740960954]
    })

    objects = PublicationManager()

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f'{self.author} in {self.location}'


class Attachment(DatetimeCreatedMixin, AuthorMixin):
    class AttachmentType(models.TextChoices):
        PHOTO = "Photo", _("Фото")
        VIDEO = "Video", _("Видео")

    file = models.FileField('Приложение', upload_to='attachments/', validators=[validate_photo_or_video])
    file_type = models.CharField('Тип файла', choices=AttachmentType.choices, max_length=10)

    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name='Публикация')

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
