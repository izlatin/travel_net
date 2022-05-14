from django.contrib.auth import get_user_model
from django.db import models

from publications.models import Publication


class Like(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # мб здесь не каскад?



