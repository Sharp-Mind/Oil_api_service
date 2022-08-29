from django.urls import path
from mainapp import views

urlpatterns = [
    path(
        "api/v1/calculations",
        views.CalculationListAPIView.as_view(),
        name="calculations",
    ),
    path(
        "api/v1/calculations/<str:cid>",
        views.SingleCalculationListAPIView.as_view(),
        name="single_calculation",
    ),
]
