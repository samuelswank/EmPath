from django.shortcuts import render
import signal
import os

# Create your views here.


def index(request):
    return render(request, "SearchTracker/index.html")


def close(request):
    # Get the process group ID of the current process
    pgid = os.getpgid(os.getpid())
    # Send SIGKILL to every process in this group
    os.killpg(pgid, signal.SIGKILL)
