from rest_framework import serializers
from .models import (
    WeatherMasterXCoordinates,
    WeatherMasterXLocation,
    WeatherMasterXReadings,
    WeatherMasterX,
)


class WeatherMasterXCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherMasterXCoordinates
        fields = ["lat", "lon"]


class WeatherMasterXLocationSerializer(serializers.ModelSerializer):
    coordinates = WeatherMasterXCoordinatesSerializer()

    class Meta:
        model = WeatherMasterXLocation
        fields = ["city_name", "coordinates"]

    def create(self, validated_data):
        coordinates_data = validated_data.pop("coordinates")
        coordinates = WeatherMasterXCoordinates.objects.create(**coordinates_data)
        return WeatherMasterXLocation.objects.create(
            coordinates=coordinates, **validated_data
        )


class WeatherMasterXReadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherMasterXReadings
        fields = [
            "temp_fahrenheit",
            "humidity_percent",
            "pressure_hpa",
            "uv_index",
            "rain_mm",
        ]


class WeatherMasterXSerializer(serializers.ModelSerializer):
    location = WeatherMasterXLocationSerializer()
    readings = WeatherMasterXReadingsSerializer()

    class Meta:
        model = WeatherMasterX
        fields = "__all__"

    def create(self, validated_data):
        location_data = validated_data.pop("location")
        readings_data = validated_data.pop("readings")

        location = self.fields["location"].create(location_data)
        readings = WeatherMasterXReadings.objects.create(**readings_data)

        weather_master_x = WeatherMasterX.objects.create(
            location=location, readings=readings, **validated_data
        )
        return weather_master_x
