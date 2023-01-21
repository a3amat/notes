from django.shortcuts import render

from .models import *


def article(request):
    obj = "Hello world, article"
    context = {
        'obj': obj
    }
    return render(request, 'article/home.html', context)
