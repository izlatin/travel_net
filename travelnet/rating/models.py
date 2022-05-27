from django.db import models

from core.mixins import DatetimeCreatedMixin, VisibleMixin, AuthorMixin
from rating.managers import CommentManager, CommentLikeManager, FollowingRelationManager
from rating.managers import PublicationLikeManager
from users.models import CustomUser


class Comment(AuthorMixin, DatetimeCreatedMixin, VisibleMixin):
    text = models.TextField(max_length=2000)
    publication = models.ForeignKey('publications.Publication', on_delete=models.CASCADE)
    # TODO: change responding_to from cascade to something else
    responding_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    objects = CommentManager()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class PublicationLike(AuthorMixin, DatetimeCreatedMixin):
    publication = models.ForeignKey('publications.Publication', on_delete=models.CASCADE)

    objects = PublicationLikeManager()

    class Meta:
        verbose_name = 'Лайк на публикации'
        verbose_name_plural = 'Лайки на публикациях'
        constraints = [
            models.UniqueConstraint(fields=['publication', 'author'], name='unique_like_per_user_per_publication')
        ]


class CommentLike(AuthorMixin, DatetimeCreatedMixin):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    objects = CommentLikeManager()

    class Meta:
        verbose_name = 'Лайк на комментарии'
        verbose_name_plural = 'Лайки на комментариях'
        constraints = [
            models.UniqueConstraint(fields=['comment', 'author'], name='unique_like_per_user_per_comment')
        ]


class FollowingRelation(DatetimeCreatedMixin):
    subscriber = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE, verbose_name='Подписчик')
    author = models.ForeignKey(CustomUser, related_name='subscribers', on_delete=models.CASCADE, verbose_name='Креатор контента')

    objects = FollowingRelationManager()

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(fields=['subscriber', 'author'], name='unique_following_relation')
        ]


