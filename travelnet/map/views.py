from django.shortcuts import render
from django.views.generic import TemplateView
from publications.models import Publication
from publications.serializers import PublicationSerializer
from travelnet.settings import MAPBOX_TOKEN


class PostsView(TemplateView):
    template_name = "map/posts.html"

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)

        token = MAPBOX_TOKEN
        posts = Publication.objects.popular_posts(100)

        prepared_posts = []
        for post in posts:
            post = PublicationSerializer(post).data
            prepared_posts.append(post)

        context['posts'] = prepared_posts
        context['token'] = token

        return context
