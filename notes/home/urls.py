from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'Home'

urlpatterns = [
    path('', home, name='base_home'),
]
