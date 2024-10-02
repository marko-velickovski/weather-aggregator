from rest_framework import serializers
from .models import BulgarianMeteoPro


class BulgarianMeteoProSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulgarianMeteoPro
        fields = "__all__"
