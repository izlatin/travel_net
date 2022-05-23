from django.db import models
from django.db.models import Count


class PublicationQueryset(models.QuerySet):
    def select_and_prefetch(self):
        res = self.select_related('location').select_related('author').prefetch_related('publicationlike_set') \
                   .prefetch_related('comment_set').prefetch_related('comment_set__commentlike_set') \
                   .prefetch_related('comment_set__author').prefetch_related('publicationlike_set__author')
        return res


class PublicationManager(models.Manager):
    def get_queryset(self):
        return PublicationQueryset(model=self.model, using=self._db)

    def popular_posts(self, post_count, datetime_created_after):
        return self.get_queryset().select_and_prefetch() \
                   .filter(visible=True, datetime_created__gt=datetime_created_after) \
                   .annotate(publicationlike_count=Count('publicationlike')) \
                   .order_by('publicationlike_count', '-datetime_created')[:post_count]

    def user_feed(self, user, post_count):
        return self.get_queryset().filter(visible=True, author__in=user.follows.all()) \
                   .order_by('-datetime_created')[:post_count]
