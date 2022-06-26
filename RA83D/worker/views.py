import json

from django.shortcuts import render
from django.shortcuts import HttpResponse, Http404
import os
from django.views.decorators.csrf import csrf_exempt

worker = os.getenv('WORKER_NAME', '0')


@csrf_exempt
def work(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        with open('token', 'w') as f:
            f.write(str(data))
            f.close()

        return HttpResponse(200)
    raise Http404


def req(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print('received post: ', data)
        with open('req', 'a+') as f:
            f.write(str(data)+"\n")
            f.close()

        return HttpResponse(200)
    raise Http404


def homepage(request):
    if request.method == 'GET':
        return HttpResponse('<h2>worker: {}</h2>'.format(worker))
    raise Http404



