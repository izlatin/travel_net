from django.http import HttpResponse
from rest_framework import generics, status, mixins
from rest_framework.response import Response

from rating.models import PublicationLike, CommentLike
from rating.serializers import PublicationLikeSerializer, CommentSerializer, CommentLikeSerializer


class PublicationLikeViews(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = PublicationLikeSerializer

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponse(status=401)
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        try:
            PublicationLike.objects.get(publication_id=request.data.get('publication'), author=request.user).delete()
        except PublicationLike.DoesNotExist:
            return HttpResponse(status=400)
        return HttpResponse(status=200)


class CommentLikeViews(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = CommentLikeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        try:
            CommentLike.objects.get(comment_id=request.data.get('comment'), author=request.user).delete()
        except CommentLike.DoesNotExist:
            return HttpResponse(status=400)
        return HttpResponse(status=200)


class CommentViews(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    serializer_class = CommentSerializer
    queryset = PublicationLike.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = serializer.data
        data.update({'comment_id': serializer.instance.id})
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
