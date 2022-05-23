from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse
from rest_framework import generics, serializers
from rest_framework import mixins

from rating.models import PublicationLike, Comment
from rating.serializers import PublicationLikeSerializer, CommentSerializer


class PublicationLikeViews(generics.GenericAPIView):
    serializer_class = PublicationLikeSerializer
    queryset = PublicationLike.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            PublicationLike.objects.create(publication_id=request.data.get('publication_id'), author=request.user)
        except (ValidationError, IntegrityError):
            return HttpResponse(status=400)
        return HttpResponse(status=200)

    def delete(self, request, *args, **kwargs):
        try:
            PublicationLike.objects.get(publication_id=request.data.get('publication_id'), author=request.user).delete()
        except PublicationLike.DoesNotExist:
            return HttpResponse(status=400)
        return HttpResponse(status=200)


class CommentViews(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    serializer_class = CommentSerializer
    queryset = PublicationLike.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        # try:
        #     Comment.objects.create(publication_id=request.data.get('publication_id'), text=request.data.get('text'), author=request.user)
        # except (ValidationError, IntegrityError):
        #     return HttpResponse(status=400)
        # return HttpResponse(status=200)

    def delete(self, request, *args, **kwargs):
        # return self.destroy(request, *args, **kwargs)
        try:
            PublicationLike.objects.get(publication_id=request.data.get('publication_id'), author=request.user).delete()
        except PublicationLike.DoesNotExist:
            return HttpResponse(status=400)
        return HttpResponse(status=200)
