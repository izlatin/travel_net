from django.contrib.auth import get_user_model
from django.db import models

from publications.models import Publication, AuthorMixin, DatetimeCreatedMixin, VisibleMixin


class CommentManager(models.Manager):
    def popular_comments(self, publication: Publication, count: int):
        return self.filter(publication=publication, visible=True).order_by('commentlike')[:count]


class Comment(AuthorMixin, DatetimeCreatedMixin, VisibleMixin):
    text = models.TextField(max_length=2000)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    # TODO: change responding_to from cascade to something else
    responding_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    objects = CommentManager()


class PublicationLike(AuthorMixin, DatetimeCreatedMixin):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)


class CommentLike(AuthorMixin, DatetimeCreatedMixin):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

