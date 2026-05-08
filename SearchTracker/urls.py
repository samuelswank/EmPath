from django.urls import path
from . import views

app_name = "SearchTracker"

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path("close/", views.close, name="close"),
]
