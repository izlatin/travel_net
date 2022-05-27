from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

# Register your models here.
from publications.models import Attachment, Publication

admin.site.register(Publication, MapAdmin)
admin.site.register(Attachment)
