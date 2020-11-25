import factory
from factory.fuzzy import FuzzyChoice
from ingredients_core.models import IngredientCore


class IngredientFactoryCore(factory.django.DjangoModelFactory):
    class Meta:
        model = IngredientCore

    ingredients = factory.Faker("text")
    allergens = factory.Faker("text")
    dietary_info = FuzzyChoice(IngredientCore.DIETARY_INFO_CHOICES)
