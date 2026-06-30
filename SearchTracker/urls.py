from django.urls import path
from . import views

app_name = "SearchTracker"

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path("applications/", views.ApplicationsTemplateView.as_view(),
         name="applications"),
    path("documents/", views.documents, name="documents"),
    path("documents/id=<int:pk>",
         views.DocumentDetailView.as_view(), name="document_detail"),
    path("documents/pdf/filename=<str:filename>",
         views.display_pdf, name="display_pdf"),
    path("template-snippets/delete/id=<int:pk>",
         views.delete_snippet, name="delete_snippet"),
    path("contacts/", views.ContactListView.as_view(), name="contacts"),
    path("contacts/id=<int:pk>/icon/change/",
         views.change_contact_icon, name="change_contact_icon"),
    path("contacts/<slug>", views.ContactDetailView.as_view(), name="contact_detail"),
    path("admin-api/", views.admin_api, name="admin_api"),
    # path("heartbeat/", views.heartbeat, name="heartbeat"),
    path("open-browser/", views.open_browser, name="open_browser"),
    path("close/", views.close, name="close"),
]
