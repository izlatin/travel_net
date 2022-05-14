from django.db import models

from travelnet.publications.models import Publication
from travelnet.users.models import CustomUser


class Like(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # мб здесь не каскад?



