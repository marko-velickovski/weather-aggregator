from django.db import models


class BulgarianMeteoPro(models.Model):
    station_id = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()
    temperature_celsius = models.FloatField()
    humidity_percent = models.FloatField()
    wind_speed_kph = models.FloatField()
    station_status = models.CharField(max_length=50)
