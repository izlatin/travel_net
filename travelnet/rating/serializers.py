from rest_framework import serializers

from rating.models import PublicationLike, Comment


class PublicationLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationLike
        fields = ['publication_id']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    # publication = serializers.PrimaryKeyRelatedField(
    #     read_only=True
    # )

    class Meta:
        model = Comment
        fields = ['publication', 'text', 'author']
