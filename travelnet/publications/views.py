from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView

from publications.models import Publication

from publications.forms import CreatePublicationForm


class PublicationList(ListView):
    model = Publication
    template_name = 'publications/publication_list.html'
    context_object_name = 'publications'

    def get_queryset(self):
        post_count = 5

        # если чел разлогинен или у него 0 подписок, кидаем популярные посты
        # иначе кидаем посты из подписок
        if not self.request.user.is_authenticated or self.request.user.follows.count() == 0:
            return Publication.objects.popular_posts(post_count)
        return Publication.objects.popular_posts(post_count)

        return Publication.objects.user_feed(self.request.user, post_count)

    def post(self):
        # TODO: либо добавляем через ajax, тогда здесь пусто должно быть потому что ссылка для
        #  лайков будет чет вроде /api/v1/likes/add, либо добавялем лайки без аджакса и тогда
        #  здесь обработка всего этого
        pass


def create_publication(request):
    if request.method == 'POST':
        form = CreatePublicationForm(request.POST)
        if form.is_valid():
            post = Publication.objects.create(
                text=form.cleaned_data['text'],
                location=form.cleaned_data['location'],
                author=request.user)
            post.save()
            return redirect(reverse('users:user_detail', kwargs={'user_id': request.user.id}))
    else:
        form = CreatePublicationForm()
    context = {'form': form}
    return render(request, 'publications/create_publication.html', context)
