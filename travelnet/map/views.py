from django.shortcuts import render
from django.views.generic import TemplateView


class PostsView(TemplateView):
    template_name = "map/posts.html"
