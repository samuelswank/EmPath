from django.views.generic import TemplateView
from .models import Document, TemplateSnippet
from django.shortcuts import render
import os
import signal
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# helper constants

APP_NAME = "SearchTracker"
ADMIN_PREFIX = f"/admin/{APP_NAME}/"

# class based views


class HomeTemplateView(TemplateView):
    template_name = f"{APP_NAME}/home.html"

# function based views


def documents(request):
    return render(request, f"{APP_NAME}/documents.html", {
        "documents": Document.objects.all(),
        "documents_count": Document.objects.count(),
        "add_document_url": f"{ADMIN_PREFIX}document/add/",
        "snippets": TemplateSnippet.objects.all(),
        "snippets_count": TemplateSnippet.objects.count(),
        "add_snippet_url": f"{ADMIN_PREFIX}templatesnippet/add/",
    })

# utility views


@csrf_exempt
def close(request):
    # Get the process group ID of the current process
    pgid = os.getpgid(os.getpid())
    # Send SIGKILL to every process in this group
    os.killpg(pgid, signal.SIGKILL)
