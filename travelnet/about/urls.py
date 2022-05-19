from django.urls import path
from .views import description, faq

app_name = 'about'
urlpatterns = [
    path('', description, name="description"),
    path('faq/', faq, name="faq")
]
