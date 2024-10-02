from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    WeatherMasterXViewSet,
)

router = DefaultRouter()
router.register("", WeatherMasterXViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
