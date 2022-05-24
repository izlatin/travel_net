import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from publications.forms import CreatePublicationForm
from publications.models import Publication, Attachment


class PublicationList(ListView):
    model = Publication
    template_name = 'publications/publication_list.html'
    context_object_name = 'publications'

    def get_queryset(self):
        post_count = 5
        datetime_most_popular_created_before = datetime.datetime.now() - datetime.timedelta(days=14)

        # если чел разлогинен или у него 0 подписок, кидаем популярные посты
        # иначе кидаем посты из подписок
        # if not self.request.user.is_authenticated or self.request.user.follows.count() == 0:
        #     return
        q1 = Publication.objects.user_feed(self.request.user, post_count)
        q2 = Publication.objects.popular_posts(post_count, datetime_created_after=datetime_most_popular_created_before)
        res = (q1 & q2).distinct()
        return res

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
    success_url = reverse_lazy('publications:publication_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        publication = form.save(commit=False)
        publication.author = self.request.user
        publication.save()

        files = self.request.FILES.getlist('file')
        if form.is_valid():
            for f in files:
                Attachment.objects.create(
                    author=self.request.user, publication_id=publication.id, file_type='Photo', file=f
                )

        return super().form_valid(form)

# class AttachmentListView(ListView):
#     template_name = 'publications/attachments.html'
#
#     def get(self, request, publication_id, *args, **kwargs):
#         self.queryset = Attachment.objects.filter(publication_id=publication_id)
#         return super().get(request, *args, **kwargs)
