from django.contrib.auth import get_user_model
from model_bakery.recipe import Recipe, foreign_key

from publications.models import Location
from publications.models import Publication

user = Recipe(get_user_model(), username='lloocchh')
location = Recipe(Location)
post_izlatin = Recipe(
    Publication,
    id=1,
    visible=1,
    author=foreign_key(user),
    location=foreign_key(location),
)
