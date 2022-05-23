import datetime

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from publications.forms import CreatePublicationForm
from publications.models import Publication


class PublicationList(ListView):
    model = Publication
    template_name = 'publications/publication_list.html'
    context_object_name = 'publications'

    def get_queryset(self):
        post_count = 5
        datetime_most_popular_created_before = datetime.datetime.now() - datetime.timedelta(days=14)

        # если чел разлогинен или у него 0 подписок, кидаем популярные посты
        # иначе кидаем посты из подписок
        if not self.request.user.is_authenticated or self.request.user.follows.count() == 0:
            return Publication.objects.popular_posts(post_count,
                                                     datetime_created_after=datetime_most_popular_created_before)
        return Publication.objects.popular_posts(post_count,
                                                 datetime_created_after=datetime_most_popular_created_before)

        return Publication.objects.user_feed(self.request.user, post_count)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['new_publication_form'] = CreatePublicationForm()
        return context


class DetailedPublicationView(DetailView):
    model = Publication
    template_name = 'publications/publication_detail.html'
    context_object_name = 'post'

    queryset = Publication.objects.get_queryset().select_and_prefetch()


class CreatePublicationView(CreateView):
    model = Publication
    template_name = 'publications/create_publication.html'
    form_class = CreatePublicationForm

    # def post(self, request):
    #     form = CreatePublicationForm(request.POST)
    #     if form.is_valid():
    #         post = Publication.objects.create(
    #             text=form.cleaned_data['text'],
    #             location=form.cleaned_data['location'],
    #             author=request.user)
    #         post.save()
    #         return redirect(reverse('users:user_detail', kwargs={'user_id': request.user.id}))


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
