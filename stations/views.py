from rest_framework.views import APIView
from rest_framework.response import Response
from bulgarian_meteo_pro.models import BulgarianMeteoPro
from weather_master_x.models import WeatherMasterX
from bulgarian_meteo_pro.serializers import BulgarianMeteoProSerializer
from weather_master_x.serializers import WeatherMasterXSerializer


class AggregationView(APIView):
    def get(self, request, city_name):
        station_data = list()
        total_temp = 0
        total_humidity = 0
        total_wind_speed = 0
        average_temperature_celsius = 0
        average_humidity_percent = 0
        average_wind_speed_kph = 0

        bulgarian_meteo_stations = BulgarianMeteoPro.objects.filter(city=city_name)
        for station in bulgarian_meteo_stations:
            serializer = BulgarianMeteoProSerializer(station)
            station_dict = {
                **serializer.data,
                "station_type": "BulgarianMeteoPro",
            }
            station_data.append(station_dict)

            total_temp += station.temperature_celsius
            total_humidity += station.humidity_percent
            total_wind_speed += station.wind_speed_kph

        weather_master_stations = WeatherMasterX.objects.filter(
            location__city_name=city_name
        ).select_related("location", "readings")
        for station in weather_master_stations:
            serializer = WeatherMasterXSerializer(station)
            station_dict = {
                **serializer.data,
                "station_type": "WeatherMasterX",
            }
            station_data.append(station_dict)

            total_temp += (station.readings.temp_fahrenheit - 32) * 5.0 / 9.0
            total_humidity += station.readings.humidity_percent
            total_wind_speed += station.readings.pressure_hpa

        station_count = len(station_data)
        if station_count > 0:
            average_temperature_celsius = total_temp / station_count
            average_humidity_percent = total_humidity / station_count
            average_wind_speed_kph = total_wind_speed / station_count

        response_data = {
            "city": city_name,
            "average_temperature_celsius": average_temperature_celsius,
            "average_humidity_percent": average_humidity_percent,
            "average_wind_speed_kph": average_wind_speed_kph,
            "station_data": station_data,
        }

        return Response(response_data)
