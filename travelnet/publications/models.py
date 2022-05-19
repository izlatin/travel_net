from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields.files import FieldFile
from django.utils.translation import ugettext_lazy as _


# TODO: move these mixins to a separate file
class DatetimeCreatedMixin(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class VisibleMixin(models.Model):
    visible = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AuthorMixin(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=50, null=True)
    building = models.CharField(max_length=10, null=True)

    place_alias = models.CharField('Название места/заведения', max_length=150, null=True, blank=True)


class PublicationManager(models.Manager):
    def popular_posts(self, post_count):
        # TODO: try to make a better "popular posts" algorithm, maybe use some metadata?
        return self.filter(visible=True).prefetch_related('publicationlike_set').prefetch_related(
            'comment_set').order_by('-publicationlike', '-datetime_created')[:post_count]

    def user_feed(self, user, post_count):
        return self.filter(visible=True).prefetch_related('publicationlike_set').prefetch_related(
            'publication_set').filter(author__in=user.follows.all()).order_by('-datetime_created')[:post_count]


class Publication(AuthorMixin, DatetimeCreatedMixin, VisibleMixin):
    text = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    objects = PublicationManager()


def validate_photo_or_video(obj: FieldFile):
    # not sure if this works
    extension = obj.name.split('.')[-1]
    if extension not in ('png', 'jpg', 'mp4', 'webm'):
        raise ValidationError(_('Файл который вы передали не является фото/видео. '
                                'Поддерживаемые форматы: png, jpg, mp4, webm.'))


class Attachment(DatetimeCreatedMixin, AuthorMixin):
    class AttachmentType(models.TextChoices):
        PHOTO = "Photo", _("Фото")
        VIDEO = "Video", _("Видео")

    file = models.FileField('Приложение', upload_to='attachments/', validators=[validate_photo_or_video])
    file_type = models.CharField('Тип файла', choices=AttachmentType.choices, max_length=10)
