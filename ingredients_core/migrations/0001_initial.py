# Generated by Django 3.1.3 on 2020-11-23 18:46

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LifeStyleCore",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="e.g: Vegan, Vegetarian, Kosher and etc",
                        max_length=15,
                    ),
                ),
            ],
        )
    ]
