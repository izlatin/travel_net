import datetime

from django.db import models
from django.db.models import Count, Q

from rating.models import FollowingRelation


class PublicationQueryset(models.QuerySet):
    def select_and_prefetch(self):
        res = self.select_related('author').prefetch_related('publicationlike_set') \
            .prefetch_related('comment_set').prefetch_related('comment_set__commentlike_set') \
            .prefetch_related('comment_set__author').prefetch_related('publicationlike_set__author')
        return res


class PublicationManager(models.Manager):
    def get_queryset(self):
        return PublicationQueryset(model=self.model, using=self._db)

    def popular_posts(self, datetime_created_after=(datetime.datetime.now() - datetime.timedelta(days=14))):
        return self.get_queryset().select_and_prefetch() \
            .filter(visible=True, datetime_created__gt=datetime_created_after) \
            .annotate(publicationlike_count=Count('publicationlike')) \
            .order_by('-publicationlike', '-datetime_created')

    def user_feed(self, user):
        return self.get_queryset().select_and_prefetch().filter(visible=True).filter(
            Q(author_id__in=FollowingRelation.objects.get_subscription_queryset_from_user(user)) | Q(author=user)).order_by('-datetime_created')
