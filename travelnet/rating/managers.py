from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models import Count

from publications.models import Publication


class CommentManager(models.Manager):
    def popular_comments(self, publication: Publication, count: int):

        return self.filter(publication=publication, visible=True).annotate(like_count=Count('commentlike'))\
               .order_by('like_count', '-datetime_created')[:count]


class PublicationLikeManager(models.Manager):
    def users_liked_list(self):
        return self.values_list('author_id', flat=True)
