from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BulgarianMeteoProViewSet

router = DefaultRouter()
router.register("", BulgarianMeteoProViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
