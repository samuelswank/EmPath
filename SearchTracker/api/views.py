from rest_framework import generics
from ..models import Contact, ContactIcon
from .serializers import ContactIconSerializer, ContactSerializer
from django.db.models import Q


class ContactDetails(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "pk"


class ContactIconFemaleList(generics.ListAPIView):
    queryset = ContactIcon.objects.filter(
        Q(icon_sex="Female") | Q(icon_sex="Either"))
    serializer_class = ContactIconSerializer


class ContactIconMaleList(generics.ListAPIView):
    queryset = ContactIcon.objects.filter(
        Q(icon_sex="Male") | Q(icon_sex="Either"))
    serializer_class = ContactIconSerializer
