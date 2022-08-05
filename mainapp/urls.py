from django.urls import path
from mainapp import views

urlpatterns = [
    path("reports/report_info", views.ReportsListAPIView.as_view()),
]
