from django.urls import path
from .views import AggregationView

urlpatterns = [
    path(
        "aggregate-city-weather/<str:city_name>/",
        AggregationView.as_view(),
        name="aggregate_city_weather",
    ),
]
