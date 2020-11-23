from django.db import models


class LifeStyleCore(models.Model):
    """
    Lifestyle Core
    """

    name = models.CharField(
        max_length=15, help_text="e.g: Vegan, Vegetarian, Kosher and etc"
    )

    def __str__(self):
        return self.name


class IngredientCore(models.Model):
    """
    Ingredient Core model
    """

    list_of_ingredients = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        help_text="If items are not used",
    )
    allergens = models.CharField(max_length=50, null=True, blank=True)
    life_style = models.ForeignKey(
        LifeStyleCore, null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True

    def get_ingredients_items(self):
        # Not using the IngredientItemCore
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
