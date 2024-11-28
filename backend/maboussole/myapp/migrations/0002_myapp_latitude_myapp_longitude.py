# Generated by Django 5.1.3 on 2024-11-28 00:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="myapp",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="myapp",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]