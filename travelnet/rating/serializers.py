from rest_framework import serializers

from rating.models import PublicationLike, Comment, CommentLike


class PublicationLikeSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = PublicationLike
        fields = ['publication', 'author']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Comment
        fields = ['publication', 'text', 'author']


class CommentLikeSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = CommentLike
        fields = ['comment', 'author']
