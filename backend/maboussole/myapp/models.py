from django.db import models

class MyApp(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    price_level = models.IntegerField()
    opening_hours = models.JSONField(null=True, blank=True)
    photos = models.JSONField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.name
