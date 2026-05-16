from django.urls import path
from . import views

app_name = "SearchTracker"

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path("documents/", views.documents, name="documents"),
    path("template-snippets/delete/id=<int:pk>",
         views.delete_template_snippet, name="delete_template_snippet"),
    path("contacts/", views.ContactListView.as_view(), name="contacts"),
    # path("heartbeat/", views.heartbeat, name="heartbeat"),
    path("close/", views.close, name="close"),
]
