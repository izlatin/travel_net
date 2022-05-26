from django.urls import path

from .views import PublicationList, CreatePublicationView, DetailedPublicationView

app_name = 'publications'
urlpatterns = [
    path('', PublicationList.as_view(), name='publication_list'),
    path('create/', CreatePublicationView.as_view(), name='create_publication'),
    path('<int:pk>/', DetailedPublicationView.as_view(), name='detail_publication'),
]
