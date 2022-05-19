from django.contrib import admin

from .models import PublicationLike, CommentLike, Comment

admin.site.register(PublicationLike)
admin.site.register(CommentLike)
admin.site.register(Comment)
