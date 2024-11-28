from django.db import models

class MyApp(models.Model):
    location_id = models.CharField(max_length=255, unique=True, default="UNKNOWN")  # Default value added
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    price_level = models.IntegerField()
    opening_hours = models.JSONField(null=True, blank=True)
    photos = models.JSONField(null=True, blank=True)
    review_rating_count = models.JSONField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    last_fetched = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


