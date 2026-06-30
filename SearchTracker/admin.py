from django.contrib import admin
from .models import *

# Inline classes


class ContactEmployerTitleInline(admin.TabularInline):
    model = ContactEmployerTitle
    extra = 1
    exclude = ("created_at", "updated_at", )

# Custom Admin classes


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    inlines = [ContactEmployerTitleInline, ]
    exclude = ("employers", "job_titles", )


class EmployerAdmin(admin.ModelAdmin):
    exclude = ("contacts", "created_at", "updated_at", )


class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication
    exclude = ("job_application_location", )

    list_display = ("position_title", "requisition_number",
                    "employer", "status",)

    list_editable = ("status",)


# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactIcon)
admin.site.register(Document)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(Location)
admin.site.register(Title)
admin.site.register(Snippet)
