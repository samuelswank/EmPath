from django.contrib import admin
from .models import Contact, ContactIcon, Document, Snippet, Title

# Register your models here.
admin.site.register(Contact)
admin.site.register(ContactIcon)
admin.site.register(Document)
admin.site.register(Title)
admin.site.register(Snippet)
