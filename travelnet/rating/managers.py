from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from publications.models import Publication


class CommentManager(models.Manager):
    def popular_comments(self, publication: Publication, count: int):
        return self.filter(publication=publication, visible=True).order_by('commentlike')[:count]


class PublicationLikeManager(models.Manager):
    def users_liked_list(self):
        xd = self.values('author')
        return [i['author'] for i in xd]

