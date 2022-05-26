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
            attachment = None
            attachment_link = None

            for at in post.attachment_set.all():
                if at.file_type == "Photo":
                    attachment = at
                    break
            if attachment and attachment.file_type == "Photo":
                attachment_link = attachment.file.url
            post = PublicationSerializer(post).data
            post["url_for"] = reverse('publications:detail_publication', kwargs={'pk': post['id']})
            post['attachment'] = attachment_link
            prepared_posts.append(post)
        context['posts'] = prepared_posts
        context['token'] = token

        return context
