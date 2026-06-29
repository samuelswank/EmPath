import django_filters
from .models import Contact


class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ("given_name", "surname",)

    given_name = django_filters.CharFilter(
        "given_name", lookup_expr="icontains", label="Given Name")

    surname = django_filters.CharFilter(
        "surname", lookup_expr="icontains", label="Surname")

    employment_history = django_filters.CharFilter(
        "employment_history__employer__name", lookup_expr="icontains", label="Employer")

    job_titles = django_filters.CharFilter(
        "employment_history__title__title", lookup_expr="icontains", label="Job Title")
