from django.db import models


class IngredientCore(models.Model):
    """
    Ingredient Core model
    """

    VEGAN = "VEGAN"
    VEGETARIAN = "VEGETARIAN"
    KOSHER = "KOSHER"

    LIFE_STYLE_CHOICES = (
        (VEGAN, "Vegan"),
        (VEGETARIAN, "Vegetarian"),
        (KOSHER, "Kosher"),
    )

    list_of_ingredients = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="If items are not used",
    )
    allergens = models.CharField(max_length=50, null=True, blank=True)
    life_style = models.CharField(
        max_length=30, choices=LIFE_STYLE_CHOICES, null=True, blank=True
    )

    class Meta:
        abstract = True

    def get_ingredients_items(self):
        # Using list_of_ingredients
        if self.list_of_ingredients:
            return self.list_of_ingredients


# TODO - phase2 if we need in the future by item
# class IngredientItemCore(models.Model):
#     """
#     Ingredient Item Core
#     """
#     ingredient_name = models.CharField(max_length=20)
#     amount = models.CharField(max_length=6)
#     is_allergen = models.Boolean(default=False)
#     display_hierarchy = models.IntegerField(default=0)
#
#     class Meta:
#         abstract = True
