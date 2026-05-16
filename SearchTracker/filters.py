import django_filters
from .models import Contact


class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ("surname", "given_name", "employers", "job_titles")

    employers = django_filters.CharFilter(
        "employer__name", lookup_expr="icontains", label="Employer")

    job_titles = django_filters.CharFilter(
        "title__title", lookup_expr="icontains", label="Job Title")
