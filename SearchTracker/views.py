from django.views.generic import DetailView, ListView, TemplateView
from .models import Contact, ContactIcon, Document, Snippet
from .filters import ContactFilter
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import Http404, FileResponse, HttpResponse, JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import webbrowser
import os
import signal


# Create your views here.

# helper constants

APP_NAME = "SearchTracker"
ADMIN_PREFIX = f"/admin/{APP_NAME}/"


# class based views

# abstract class based views

class FilteredListView(ListView):
    """
    From Dan Poirier's "Dan's Cheat Sheets"
    https://cheat.readthedocs.io/en/latest/index.html
    """
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset)

        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filterset"] = self.filterset
        return context

# Template Views


class HomeTemplateView(TemplateView):
    template_name = f"{APP_NAME}/home.html"

# ListViews


class ContactListView(FilteredListView):
    model = Contact
    context_object_name = "contacts"
    filterset_class = ContactFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_url"] = f"{ADMIN_PREFIX}contact/add/"

        return context

# DetailViews


class ContactDetailView(DetailView):
    model = Contact
    context_object_name = "contact"


class DocumentDetailView(DetailView):
    model = Document
    context_object_name = "document"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filename"] = self.object.get_filename()
        return context

# function based views


def documents(request):
    return render(request, f"{APP_NAME}/documents.html", {
        "documents": Document.objects.all(),
        "documents_count": Document.objects.count(),
        "add_document_url": f"{ADMIN_PREFIX}document/add/",
        "snippets": Snippet.objects.all(),
        "snippets_count": Snippet.objects.count(),
        "add_snippet_url": f"{ADMIN_PREFIX}snippet/add/",
    })


@require_http_methods(["POST"])
def change_contact_icon(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    icon_id = request.POST.get("icon-id")
    if not icon_id:
        return JsonResponse({"success": False, "error": "Missing icon_id"}, status=400)

    try:
        new_icon = ContactIcon.objects.get(pk=icon_id)
    except ContactIcon.DoesNotExist:
        return JsonResponse({"success": False, "error": "Invalid icon ID"}, status=400)

    contact.contact_icon = new_icon
    contact.save()

    return JsonResponse({"success": True, "redirect_url": reverse_lazy(f"{APP_NAME}:contacts")})


def delete_snippet(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
        if request.method == "POST":
            snippet.delete()
            return redirect(f"{APP_NAME}:documents")
    except Snippet.DoesNotExist:
        raise Http404(f"Snippet with id={pk} does not exist")

# utility views


@xframe_options_exempt
def display_pdf(request, filename):
    try:
        pdf_path = os.path.join(
            settings.BASE_DIR, "media", "SearchTracker", "files", "pdfs", filename)
        response = FileResponse(open(pdf_path, "rb"),
                                content_type="application/pdf")
        response["Content-Disposition"] = f"inline; filename={filename}"
        return response
    except FileNotFoundError:
        raise Http404(f"{filename} file not found")


@csrf_exempt
def open_browser(request):
    if request.method == "POST":
        url = request.POST.get("url")
        if url:
            webbrowser.open(url)
            return HttpResponse(f"Browser successfully opened to {url}")

    return HttpResponse("Invalid request", status=400)


@csrf_exempt
def close(request):
    # Get the process group ID of the current process
    pgid = os.getpgid(os.getpid())
    # Send SIGKILL to every process in this group
    os.killpg(pgid, signal.SIGKILL)
