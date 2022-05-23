from django.urls import path

from .views import PostsView

app_name = 'map'

urlpatterns = [
    path('posts/', PostsView.as_view(), name="posts")
]
