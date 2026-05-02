from django.urls import path
from . import views

app_name = "SearchTracker"

urlpatterns = [
    path('', views.index, name="index"),
    path("close/", views.close, name="close"),
]
