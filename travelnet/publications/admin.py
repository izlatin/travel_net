from django.contrib import admin

# Register your models here.
from publications.models import Location, Attachment, Publication

admin.site.register(Publication)
admin.site.register(Location)
admin.site.register(Attachment)

