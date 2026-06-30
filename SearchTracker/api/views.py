from rest_framework import generics
from ..models import Contact, ContactIcon, JobApplication
from .serializers import *
from django.db.models import Q
from rest_framework import viewsets

# Detail Views


class ContactDetails(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "pk"

# List Views


class ContactIconFemaleList(generics.ListAPIView):
    queryset = ContactIcon.objects.filter(
        Q(icon_sex="Female") | Q(icon_sex="Either"))
    serializer_class = ContactIconSerializer


class ContactIconMaleList(generics.ListAPIView):
    queryset = ContactIcon.objects.filter(
        Q(icon_sex="Male") | Q(icon_sex="Either"))
    serializer_class = ContactIconSerializer


# class JobApplicationList(generics.ListAPIView):
#     queryset = JobApplication.objects.all()
#     serializer_class = JobApplicationSerializer

# CU Views


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
