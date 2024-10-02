from rest_framework import viewsets
from .models import WeatherMasterX
from .serializers import WeatherMasterXSerializer


class WeatherMasterXViewSet(viewsets.ModelViewSet):
    queryset = WeatherMasterX.objects.all()
    serializer_class = WeatherMasterXSerializer
