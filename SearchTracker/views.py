import time
import threading
from django.views.generic import TemplateView
from .models import Document, TemplateSnippet
from django.shortcuts import render
from django.http import HttpResponse
import os
import signal
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# helper constants

APP_NAME = "SearchTracker"
ADMIN_PREFIX = f"/admin/{APP_NAME}/"

# variables
_last_heartbeat = time.time()
_heartbeat_lock = threading.Lock()
_watchdog_thread_started = False

# non view utilities


def close():
    # Get the process group ID of the current process
    pgid = os.getpgid(os.getpid())
    # Send SIGKILL to every process in this group
    os.killpg(pgid, signal.SIGKILL)


def _watchdog():
    global _last_heartbeat
    while True:
        if time.time() - _last_heartbeat > 60 * 60 * 1000:
            close()
            break

        time.sleep(5)


def _start_watchdog():
    global _watchdog_thread_started
    if not _watchdog_thread_started:
        _watchdog_thread_started = True
        thread = threading.Thread(target=_watchdog, daemon=True)
        thread.start()


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
def heartbeat(request):
    global _last_heartbeat
    with _heartbeat_lock:
        _last_heartbeat = time.time()
    _start_watchdog()
    return HttpResponse("Shutting down...")


@csrf_exempt
def close_app(request):
    close()
