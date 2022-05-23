from django.shortcuts import render
from django.views.generic import TemplateView
from publications.models import Publication
from publications.serializers import PublicationSerializer, LocationSerializer


class PostsView(TemplateView):
    template_name = "map/posts.html"

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)

        token = 'pk.eyJ1IjoiYWxleC1idWwiLCJhIjoiY2tleGNpaTI1MDAwazJ5bzJucWgyMmh3aiJ9.N1pXrpkKMv4NfecZmZa3TA'
        posts = Publication.objects.popular_posts(100).select_related('location')

        prepared_posts = []
        for post in posts:
            location = post.location
            post = PublicationSerializer(post).data
            post['location'] = LocationSerializer(location).data
            prepared_posts.append(post)

        context['posts'] = prepared_posts
        context['token'] = token

        return context
