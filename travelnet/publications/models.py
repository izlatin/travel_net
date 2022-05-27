from django.db import models
from django.utils.translation import ugettext_lazy as _
from mapbox_location_field.models import LocationField

from core.mixins import AuthorMixin, DatetimeCreatedMixin, VisibleMixin
from .managers import PublicationManager


# TODO: move these mixins to a separate file


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

    file = models.ImageField('Приложение', upload_to='attachments/')
    file_type = models.CharField('Тип файла', choices=AttachmentType.choices, max_length=10)

    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name='Публикация')

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
