from django.shortcuts import render
import signal
import os

# Create your views here.


def dashboard(request):
    return render(request, "SearchTracker/dashboard.html")


def close(request):
    # Get the process group ID of the current process
    pgid = os.getpgid(os.getpid())
    # Send SIGKILL to every process in this group
    os.killpg(pgid, signal.SIGKILL)
