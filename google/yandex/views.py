from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'yandex/index.html', {'title': 'Мой первый веб-сайт'})

def denis(request):
    return render(request, 'yandex/denis.html')