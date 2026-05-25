from django.urls import include, path
from . import views

app_name = "api"

urlpatterns = [
    path("contacts/id=<int:pk>",
         views.ContactDetails.as_view(), name="contact_details"),
    path("contacts/icons/female/", views.ContactIconFemaleList.as_view(),
         name="contact_icons_female"),
    path("contacts/icons/male/", views.ContactIconMaleList.as_view(),
         name="contact_icons_male"),
]
