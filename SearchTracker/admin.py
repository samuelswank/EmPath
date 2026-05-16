from django.contrib import admin
from .models import Contact, Document, TemplateSnippet

# Register your models here.
admin.site.register(Contact)
admin.site.register(Document)
admin.site.register(TemplateSnippet)
