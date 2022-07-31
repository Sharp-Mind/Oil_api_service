from django.urls import path
from mainapp import views

urlpatterns = [
    # path('api/v1/reports', views.ReportsAPIView.as_view()),
    # path('api/v1/reports/calculate', views.calculate),
    path('reports/report_info', views.report_info),
]