from django.db import models


class IngredientCore(models.Model):
    """
    Ingredient Core model
    """

    VEGAN = "VEGAN"
    VEGETARIAN = "VEGETARIAN"
    KOSHER = "KOSHER"

    DIETARY_INFO_CHOICES = (
        (VEGAN, "Vegan"),
        (VEGETARIAN, "Vegetarian"),
        (KOSHER, "Kosher"),
    )

    ingredients = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="If items are not used",
    )
    allergens = models.CharField(max_length=50, null=True, blank=True)
    dietary_info = models.CharField(
        max_length=30, choices=DIETARY_INFO_CHOICES, null=True, blank=True
    )
    warning = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="e.g: Once defrosted, do not refreeze",
    )

    class Meta:
        abstract = True

    def get_ingredients_items(self):
        # Using list_of_ingredients
        if self.ingredients:
            return self.ingredients


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
