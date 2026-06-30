from rest_framework import serializers
from ..models import Employer, Contact, ContactIcon, JobApplication, Location, Title


class ContactIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactIcon
        exclude = ("created_at", "updated_at",)


class ContactSerializer(serializers.ModelSerializer):
    contact_icon = ContactIconSerializer(read_only=True)

    class Meta:
        model = Contact
        exclude = ("created_at", "updated_at",)


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = "__all__"


class JobApplicationSerializer(serializers.ModelSerializer):
    employer = EmployerSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    position_title = TitleSerializer(read_only=True)

    class Meta:
        model = JobApplication
        fields = "__all__"
