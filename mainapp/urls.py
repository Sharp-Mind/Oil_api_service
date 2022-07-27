from django.urls import path
from mainapp import views

urlpatterns = [
    path('api/v1/reports', views.ReportsAPIView.as_view()),
    path('api/v1/reports/post', views.ReportsAPIView.as_view()),
]


# from django.conf.urls import url
# from snippets import views

# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]