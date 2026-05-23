from django.urls import include, path
from . import views

app_name = "api"

urlpatterns = [
    path("contacts/id=<int:pk>",
         views.ContactDetails.as_view(), name="contact_details"),
]
