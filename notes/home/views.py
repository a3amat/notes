from django.shortcuts import render

from .models import *


def home(request):
    obj = "Home"
    context = {
        'obj': obj
    }
    return render(request, 'home/home.html', context)