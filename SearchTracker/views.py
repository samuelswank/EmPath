
import os
import signal
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Class based views


class HomeTemplateView(TemplateView):
    template_name = "SearchTracker/home.html"


def close(request):
    # Get the process group ID of the current process
    pgid = os.getpgid(os.getpid())
    # Send SIGKILL to every process in this group
    os.killpg(pgid, signal.SIGKILL)
