from rest_framework import generics
from ..models import Contact
from .serializers import ContactSerializer


class ContactDetails(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "pk"
