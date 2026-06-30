from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "api"

job_applications_list = views.JobApplicationViewSet.as_view({
    "get": "list",
    "post": "create"
})
job_application_detail = views.JobApplicationViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("applications/", job_applications_list, name="applications_list"),
    path("api/applications/id=<int:pk>/",
         job_application_detail, name="application_detail"),
    path("contacts/id=<int:pk>",
         views.ContactDetails.as_view(), name="contact_details"),
    path("contacts/icons/female/", views.ContactIconFemaleList.as_view(),
         name="contact_icons_female"),
    path("contacts/icons/male/", views.ContactIconMaleList.as_view(),
         name="contact_icons_male"),
]
