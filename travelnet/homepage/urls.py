from django.urls import path
from .views import feed

app_name = 'homepage'
urlpatterns = [
    path('', feed, name="home"),
]
