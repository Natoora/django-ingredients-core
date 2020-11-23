# Ingredients Core Library

*Ingredients Core is a reusable app and provides the core functionality and attributes*


Development
----------

1. Clone django-ingredients-core project.
    ```
    git clone git@github.com:Natoora/django-ingredients-core.git
    ```

2. Install library dependencies.
    ```
    pip install -r requirements.txt
    ```

3. Execute pre-commit to install the git hooks in your .git/ directory.
    ```
    pre-commit install
    ```


Testing
-------

1. Run test script:
    ```
    (venv) $ python runtests.py
    ```

How to install django-ingredients-core into your project
-----------

1. Add "ingredients-core" to your INSTALLED_APPS setting like this::
    ``` python
    INSTALLED_APPS = [
        'ingredients_core',
    ]
    ```

2. You Custom Ingredient model will be inheriting from IngredientCore:
    ```python
   from django.db import models
   from ingredients_core.models import IngredientCore

   class Ingredient(IngredientCore):
       # your custom attributes and methods
       # e.g:
       # Product or ProductBase = None
       pass

   # Important Note: if not necessary to add item by item, use the Ingredient.long_ingredients_text
   # TODO
   #class IngredientItem(IngredientItemCore):
   #    # your custom attributes and methods
   #    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ```


Releasing
---------

1. Increment version number in setup.py

2. Commit and push changes.

3. Create release on GitHub with the version number

4. The release can then be installed into Django projects like this:
    ```
    git+ssh://git@github.com/Natoora/django-ingredients-core.git@{version number}
   ```
