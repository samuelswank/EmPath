from django.urls import path
from . import views

app_name = "SearchTracker"

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path("documents/", views.documents, name="documents"),
    path("heartbeat/", views.heartbeat, name="heartbeat"),
    path("close/", views.close_app, name="close"),
]
