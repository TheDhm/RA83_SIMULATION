import json

from django.shortcuts import render, HttpResponse, Http404
from .models import Worker

app_name = "wdog"


def home(request):
    if request.method == 'GET':
        workers = Worker.objects.all()

        try:
            worker_t = workers.filter(has_token=True)[0]
        except IndexError:
            worker_t = None

        return render(request, 'wdog/home.html', {'workers': workers, 'worker_t': worker_t})
    raise Http404


def post_status(request, worker_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        has_token = data['has_token']
        token = data['token']
        req = data['req']
        in_sc = data['in_cs']

        try:
            worker = Worker.objects.get(id=worker_id)
        except Worker.DoesNotExist:
            raise Http404

        worker.token = ", ".join([str(t) for t in token])
        worker.req = ", ".join([str(r) for r in req])
        worker.has_token = has_token
        worker.in_sc = in_sc
        worker.save()

        return HttpResponse(200)
    raise Http404
