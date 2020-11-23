import factory
from tests.models import Ingredient
from ingredients_core.factories import IngredientFactoryCore


class IngredientFactory(IngredientFactoryCore):
    class Meta:
        model = Ingredient

    custom_attrib = factory.Faker("text")
