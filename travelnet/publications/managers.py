from django.db import models
from django.db.models import Count


class PublicationManager(models.Manager):
    def popular_posts(self, post_count):
        # TODO: try to make a better "popular posts" algorithm, maybe use some metadata?
        # TODO: not sure the ordering is correct here, check it (+below aswell)
        return self.filter(visible=True).prefetch_related('publicationlike_set').prefetch_related(
            'comment_set').annotate(publication_count=Count('publicationlike')).order_by(
            'publication_count', '-datetime_created')[:post_count]

    def user_feed(self, user, post_count):
        return self.filter(visible=True).prefetch_related('publicationlike_set').prefetch_related(
            'publication_set').filter(author__in=user.follows.all()).order_by('-datetime_created')[:post_count]

    def maps_posts(self):
        return self.select_related('location').filter(visible=True)
