from django.contrib.auth import get_user_model
from django.db import models

from publications.models import Publication, AuthorMixin, DatetimeCreatedMixin, VisibleMixin
from rating.managers import CommentManager


class Comment(AuthorMixin, DatetimeCreatedMixin, VisibleMixin):
    text = models.TextField(max_length=2000)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    # TODO: change responding_to from cascade to something else
    responding_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    objects = CommentManager()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class PublicationLike(AuthorMixin, DatetimeCreatedMixin):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Лайк на публикации'
        verbose_name_plural = 'Лайки на публикациях'


class CommentLike(AuthorMixin, DatetimeCreatedMixin):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Лайк на комментарии'
        verbose_name_plural = 'Лайки на комментариях'
