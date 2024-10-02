from rest_framework import viewsets
from rest_framework import viewsets
from .models import BulgarianMeteoPro
from .serializers import BulgarianMeteoProSerializer


class BulgarianMeteoProViewSet(viewsets.ModelViewSet):
    queryset = BulgarianMeteoPro.objects.all()
    serializer_class = BulgarianMeteoProSerializer
