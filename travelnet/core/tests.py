from django.test import TestCase
from model_bakery import baker

from publications.models import Publication

publication = baker.make(Publication, _quantity=2)
baker.prepare_recipe('core.post_izlatin')