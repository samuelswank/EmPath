from rest_framework import serializers
from ..models import Contact, ContactIcon


class ContactIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactIcon
        exclude = ("created_at", "updated_at",)


class ContactSerializer(serializers.ModelSerializer):
    contact_icon = ContactIconSerializer(read_only=True)

    class Meta:
        model = Contact
        exclude = ("created_at", "updated_at",)
