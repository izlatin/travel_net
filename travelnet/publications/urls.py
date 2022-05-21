from django.urls import path
from .views import PublicationList, create_publication

app_name = 'publications'
urlpatterns = [
    path('publication_list/', PublicationList.as_view(), name='publication_list'),
    path('create/', create_publication, name='create_publication')
]
