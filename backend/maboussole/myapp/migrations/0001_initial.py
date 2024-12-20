# Generated by Django 5.1.3 on 2024-11-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyApp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=255)),
                ("category", models.CharField(max_length=100)),
                ("likes", models.IntegerField(default=0)),
                ("price_level", models.IntegerField()),
                ("opening_hours", models.JSONField(blank=True, null=True)),
                ("photos", models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
