from django.db import models
from enum import Enum
from tinymce.models import HTMLField
from django.utils.html import strip_tags

# Create your models here.

# Abstract models


class TimeStampedModel(models.Model):
    """
    Abstract base class that adds created_at and updated_at fields to models.
        From Geeks for Geeks - How to Add created_at and updated_at Fields to All Django Models Using TimeStampedModel
        url: https://www.geeksforgeeks.org/python/how-to-add-created-at-and-updated-at-fields-to-all-django-models-using-timestampedmodel/
    """
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Concrete models


class Employer(TimeStampedModel):
    name = models.CharField(max_length=256)

    contacts = models.ManyToManyField(
        "Contact", related_name="contacts_by_employer")

    def __str__(self):
        return self.name


class Title(TimeStampedModel):
    title = models.CharField(max_length=128)
    min_salary = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    max_salary = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)

    resumes_for_title = models.ManyToManyField(
        "ResumeTitle", related_name="resumes_for_title")

    def __str__(self):
        return self.title


class Document(TimeStampedModel):
    class DocumentTypeOptions(Enum):
        COVER_LETTER = "Cover Letter"
        RESUME = "Resume"
        OTHER = "Other"

        @classmethod
        def choices(self):
            return [(key.value, key.name) for key in self]

    name = models.CharField(max_length=128)
    file = models.FileField()
    document_type = models.CharField(
        max_length=16, choices=DocumentTypeOptions.choices(), default=DocumentTypeOptions.RESUME)

    resume_title = models.ManyToManyField(
        "ResumeTitle", related_name="resume_title")

    def __str__(self):
        return self.name


class JobApplication(TimeStampedModel):
    class PaymentPeriodOptions(Enum):
        ANNUAL = "Annual"
        MONTHLY = "Monthly"
        HOURLY = "Hourly"
        DURATION = "Duration"

        @classmethod
        def choices(self):
            return [(key.value, key.name) for key in self]

    class StatusOptions(Enum):
        SOURCED = "Sourced"
        APPLIED = "Applied"
        INTERVIEWING = "Interviewing"
        NEGOTIATING = "Negotiating"
        ACCEPTED = "Accepted"

        @classmethod
        def choices(self):
            return [(key.value, key.name) for key in self]

    position_title = models.ForeignKey(Title, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    precise_position_title = models.CharField(
        max_length=128, blank=True, null=True)
    requisition_number = models.CharField(max_length=64, blank=True, null=True)
    original_post_link = models.URLField()
    description = HTMLField()
    description_plain = models.TextField(blank=True, editable=False)
    min_payment = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    max_payment = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    payment_period = models.CharField(
        max_length=8, choices=PaymentPeriodOptions.choices(), default=PaymentPeriodOptions.ANNUAL)
    date_sourced = models.DateTimeField()
    date_applied = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=16, choices=StatusOptions.choices(), default=StatusOptions.SOURCED)
    resume = models.ForeignKey(
        Document, on_delete=models.CASCADE, blank=True, null=True)
    notes = HTMLField()

    job_application_location = models.ManyToManyField(
        "JobApplicationLocation", related_name="job_application_location")

    def __str__(self):
        title = self.position_title
        if self.precise_position_title:
            title = self.precise_position_title

        return f"{self.employer}, {title}, {self.requisition_number}"

    def save(self, *args, **kwargs):
        self.description_plain = strip_tags(self.description)
        if not self.date_sourced or self.date_sourced == '':
            self.date_sourced = self.created_at
        super().save(*args, **kwargs)


class TemplateSnippet(TimeStampedModel):
    class SnippetTypeOptions(Enum):
        COVER_LETTER = "Cover Letter"
        DIRECT_MESSAGE = "Direct Message"
        RESUME = "Resume"

        @classmethod
        def choices(self):
            return [(key.value, key.name) for key in self]

    name = models.CharField(max_length=128)
    content = HTMLField()
    snippet_type = models.CharField(
        max_length=16, choices=SnippetTypeOptions.choices())

    def __str__(self):
        return self.name


class Contact(TimeStampedModel):
    class RelationshipOptions(Enum):
        CLASSMATE = "Classmate"
        COWORKER = "Coworker"
        INSTRUCTOR = "Instructor"
        FAMILY = "Family"
        JIAO_YOU = "教友"
        PROFESSIONAL = "Professional"
        WORKPLACE_SUPERIOR = "Workplace Superior"

        @classmethod
        def choices(self):
            return [(key.value, key.name) for key in self]

    class ContactMethodOptions(Enum):
        EMAIL = "Email"
        FACEBOOK = "Facebook"
        LINKEDIN = "LinkedIn"
        PHONE = "Phone"

        @classmethod
        def choices(self):
            return [(key.value, key.name) for key in self]

    class CitizenClassOptions(Enum):
        WORKER = "Worker"
        TALENT = "Talent"
        DRONE = "Drone"
        TECHNICIAN = "Technician"
        DOCTOR = "Doctor"
        LIBRARIAN = "Librarian"
        EMPATH = "Empath"
        THINKER = "Thinker"
        TRANSCEND = "Transcend"
        NERVE_STAPLED = "Nerve Stapled"

        @classmethod
        def choices(self):
            return [(key.value, key.name) for key in self]

    given_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64, blank=True)
    relationship = models.CharField(max_length=32, choices=RelationshipOptions.choices(
    ), default=RelationshipOptions.PROFESSIONAL)
    primary_contact = models.CharField(max_length=200)
    contact_method = models.CharField(
        max_length=8, choices=ContactMethodOptions.choices())
    citizen_type = models.CharField(
        max_length=16, choices=CitizenClassOptions.choices(), default=CitizenClassOptions.WORKER)

    def __str__(self):
        return f"{self.surname}, {self.given_name}"


class Location(TimeStampedModel):
    location_name = models.CharField(max_length=128)
    line1 = models.CharField(max_length=32, blank=True, null=True)
    line2 = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.location_name


class ResumeTitle(TimeStampedModel):
    resume = models.ForeignKey(Document, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.resume}, {self.title}"


class JobApplicationLocation(TimeStampedModel):
    job_application = models.ForeignKey(
        JobApplication, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job_application}, {self.location}"


class ContactEmployerTitle(TimeStampedModel):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, blank=True, null=True)
    current = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.contact}, {self.employer}, {self.title}"


class ActionType(TimeStampedModel):
    class ActionGroupOptions(Enum):
        INTERVIEW_PREP = "Interview Prep"
        FOLLOW_UP = "Follow Up"
        NETWORKING = "Networking"

        @classmethod
        def choices(self):
            return [(key.value, key.name) for key in self]

    action_group = models.CharField(
        max_length=16, choices=ActionGroupOptions.choices())
    action_type = models.CharField(max_length=32)
    description = HTMLField()
    description_plain = models.TextField(blank=True, editable=False)

    def __str__(self):
        return self.action_type

    def save(self, *args, **kwargs):
        self.description_plain = strip_tags(self.description)
        super().save(*args, **kwargs)


class CareerAction(TimeStampedModel):
    job_application = models.ForeignKey(
        JobApplication, on_delete=models.CASCADE, blank=True, null=True)
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, blank=True, null=True)
    action_title = models.CharField(max_length=64)
    description = HTMLField()
    description_plain = models.TextField(blank=True, editable=False)
    action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.action_title

    def save(self, *args, **kwargs):
        self.description_plain = strip_tags(self.description)
        super().save(*args, **kwargs)
