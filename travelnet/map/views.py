from django.urls import reverse
from django.views.generic import TemplateView

from publications.models import Publication
from publications.serializers import PublicationSerializer
from travelnet.settings import MAPBOX_TOKEN


class PostsView(TemplateView):
    template_name = "map/posts.html"

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)

        token = MAPBOX_TOKEN
        posts = Publication.objects.popular_posts().select_related()[:100]

        prepared_posts = []
        for post in posts:
            attachments = post.attachment_set.all()
            post = PublicationSerializer(post).data
            for at in attachments:
                if at.file_type == "Photo":
                    post['attachment'] = at.file.url
                    break
            post["url_for"] = reverse('publications:detail_publication', kwargs={'pk': post['id']})
            prepared_posts.append(post)
        context['posts'] = prepared_posts
        context['token'] = token

        return context
