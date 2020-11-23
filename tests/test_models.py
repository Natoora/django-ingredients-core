from django.test import TestCase
from .models import Ingredient
from .factories import IngredientFactory
from ingredients_core.factories import LifeStyleFactoryCore


class IngredientCoreTestCase(TestCase):
    """ Ingredient Core TestCases """

    def setUp(self):
        self.life_style = LifeStyleFactoryCore.create(name="Vegan")

        self.ingredient = IngredientFactory.create(
            list_of_ingredients="Chickpeas 50%, Extra Virgin Olive Oil 26.7% and Milk",
            allergens="This product contains milk",
            life_style=self.life_style,
            custom_attrib="Apple",
        )

    #
    # Attributes from Abstract Model
    #

    # list_of_ingredients
    def test_list_of_ingredients(self):
        self.assertEqual(
            self.ingredient.list_of_ingredients,
            "Chickpeas 50%, Extra Virgin Olive Oil 26.7% and Milk",
        )

    #  TODO, add more tests

    # allergens
    def test_allergens(self):
        self.assertEqual(
            self.ingredient.allergens, "This product contains milk"
        )

    #  TODO, add more tests

    # life_style
    def test_life_style(self):
        self.assertEqual(self.ingredient.life_style.name, "Vegan")

    #  TODO, add more tests

    #
    # Attributes from Model
    #

    # custom_attrib
    def test_custom_attrib(self):
        self.assertEqual(self.ingredient.custom_attrib, "Apple")

    #  TODO, add more tests

    #
    # Test Model Methods
    #

    def test_representation(self):
        # def __str__(self) is not implemented
        pass

    def test_get_ingredients_items(self):
        self.assertEqual(
            self.ingredient.get_ingredients_items(),
            "Chickpeas 50%, Extra Virgin Olive Oil 26.7% and Milk",
        )

    #
    # Miscellaneous
    #
    def test_create_batch(self):
        IngredientFactory.create_batch(499)
        self.assertEquals(Ingredient.objects.count(), 500)  # 499 + setUp one
