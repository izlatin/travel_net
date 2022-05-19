from rest_framework import serializers

from rating.models import PublicationLike


class PublicationLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationLike
        fields = ['publication_id']
