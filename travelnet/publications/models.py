from django.contrib.auth import get_user_model
from django.db import models


class UserSocialActionMixin(models.Model):
    # миксин для лайков / постов / чего-то аналогичного

    # мб вместо каскада поставить что-то дефолтное вроде собачки в ВК?
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=50, null=True)
    building = models.CharField(max_length=10, null=True)


class PublicationManager(models.Manager):
    def popular_posts(self):
        # TODO: try to make a better "popular posts" algorithm, maybe use some metadata?
        return self.all().filter(is_comment=False, visible=True).order_by('like').prefetch_related('like_set')[:3]


class Publication(UserSocialActionMixin):
    is_comment = models.BooleanField()
    # юзаем если есть is_comment, иначе null
    post_referred_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    objects = PublicationManager()


class Attachment(UserSocialActionMixin):
    class AttachmentType(models.IntegerChoices):
        PHOTO = 1, "Фото"
        VIDEO = 2, "Видео"

    # TODO: todo :)
    #  мб локейшен не должен