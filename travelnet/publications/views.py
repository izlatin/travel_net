from django.shortcuts import render
from django.views.generic import ListView

from publications.models import Publication


class PublicationList(ListView):
    model = Publication
    template_name = 'publications/publication_list.html'
    context_object_name = 'publications'

    def get_queryset(self):
        # если чел разлогинен или у него 0 подписок, кидаем популярные посты
        # иначе кидаем посты из подписок
        if not self.request.user.is_authenticated or self.request.user.follows.count() == 0:
            return Publication.objects.popular_posts()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # TODO: add form data here so that we can press like/dislike/add comments

        return context

