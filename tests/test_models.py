from django.test import TestCase
from .models import Ingredient
from .factories import IngredientFactory


class IngredientCoreTestCase(TestCase):
    """ Ingredient Core TestCases """

    def setUp(self):
        self.ingredient = IngredientFactory.create(
            ingredients="Chickpeas 50%, Extra Virgin Olive Oil 26.7% and Milk",
            allergens="This product contains milk",
            dietary_info=Ingredient.VEGAN,
            custom_attrib="Apple",
        )

    #
    # Attributes from Abstract Model
    #

    # ingredients
    def test_ingredients(self):
        self.assertEqual(
            self.ingredient.ingredients,
            "Chickpeas 50%, Extra Virgin Olive Oil 26.7% and Milk",
        )

    #  TODO, add more tests

    # allergens
    def test_allergens(self):
        self.assertEqual(
            self.ingredient.allergens, "This product contains milk"
        )

    #  TODO, add more tests

    # dietary_info
    def test_dietary_info(self):
        self.assertEqual(self.ingredient.dietary_info, "VEGAN")

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
