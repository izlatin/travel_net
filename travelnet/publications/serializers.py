from rest_framework import serializers

from publications.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    location = serializers.ListField()

    class Meta:
        model = Publication
        fields = "__all__"
