import factory
from ingredients_core.models import IngredientCore, LifeStyleCore


class LifeStyleFactoryCore(factory.django.DjangoModelFactory):
    class Meta:
        model = LifeStyleCore

    name = factory.Faker("text")


class IngredientFactoryCore(factory.django.DjangoModelFactory):
    class Meta:
        model = IngredientCore

    list_of_ingredients = factory.Faker("text")
    allergens = factory.Faker("text")
    life_style = factory.SubFactory(LifeStyleFactoryCore)
