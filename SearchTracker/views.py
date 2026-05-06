from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
import signal
import threading
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "SearchTracker/index.html")


@csrf_exempt
def close(request):
    def kill_proc_group():
        import time
        time.sleep(0.5)
        pgid = os.getpgid(os.getpid())
        os.killpg(pgid, signal.SIGKILL)

    threading.Thread(target=kill_proc_group, daemon=True).start()
    return HttpResponse("OK")
