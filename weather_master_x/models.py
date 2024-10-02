from django.db import models


class WeatherMasterXCoordinates(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()


class WeatherMasterXLocation(models.Model):
    city_name = models.CharField(max_length=100)
    coordinates = models.OneToOneField(
        WeatherMasterXCoordinates, on_delete=models.CASCADE
    )


class WeatherMasterXReadings(models.Model):
    temp_fahrenheit = models.FloatField()
    humidity_percent = models.FloatField()
    pressure_hpa = models.FloatField()
    uv_index = models.IntegerField()
    rain_mm = models.FloatField()


class WeatherMasterX(models.Model):
    station_identifier = models.CharField(max_length=50)
    location = models.OneToOneField(WeatherMasterXLocation, on_delete=models.CASCADE)
    recorded_at = models.DateTimeField()
    readings = models.OneToOneField(WeatherMasterXReadings, on_delete=models.CASCADE)
    operational_status = models.CharField(max_length=20)
