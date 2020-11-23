from django.db import models
from ingredients_core.models import IngredientCore


class Ingredient(IngredientCore):
    """ Test model that inherit from IngredientCore """

    custom_attrib = models.CharField(max_length=30)
