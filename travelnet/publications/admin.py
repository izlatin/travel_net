from django.contrib import admin

# Register your models here.
from publications.models import Attachment, Publication
from mapbox_location_field.admin import MapAdmin

admin.site.register(Publication, MapAdmin)
admin.site.register(Attachment)

