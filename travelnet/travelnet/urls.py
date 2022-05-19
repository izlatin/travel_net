from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from rest_framework import routers

from rating import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
  
    path('map/', include('map.urls'),
    path('publications/', include('publications.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),

    # TODO: убрать это отсюда
    path('api/v1/likes', views.PublicationLikeViews.as_view()),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

