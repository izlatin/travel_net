from django.db import models
from django.db.models import Count


class CommentManager(models.Manager):
    def order_by_like_count(self):
        return self.annotate(like_count=Count('commentlike')).order_by('-like_count', '-datetime_created')

    def popular_comments(self, publication, count: int):
        return self.filter(publication=publication, visible=True).annotate(like_count=Count('commentlike')).order_by(
            'like_count', '-datetime_created')[:count]


class PublicationLikeManager(models.Manager):
    def users_liked_list(self):
        return self.values_list('author_id', flat=True)


class CommentLikeManager(models.Manager):
    def users_liked_list(self):
        return self.values_list('author_id', flat=True)


class FollowingRelationManager(models.Manager):
    def get_subscriber_queryset_from_user(self, author):
        """ Возвращает список подписчиков какого-то креатора """
        return self.filter(author=author).values_list('subscriber_id', flat=True)

    def get_subscription_queryset_from_user(self, subscriber):
        """ Возвращает список подписок какого-то юзера """
        return self.filter(subscriber=subscriber).values_list('author_id', flat=True)
