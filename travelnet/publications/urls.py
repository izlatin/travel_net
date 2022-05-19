from django.urls import path
from .views import PublicationList

app_name = 'publications'
urlpatterns = [
    path('publication_list/', PublicationList.as_view(), name='publication_list'),
]
