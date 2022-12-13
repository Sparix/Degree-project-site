from django.shortcuts import render, HttpResponse
from .models import *


def home(request):
    categories = Categories.objects.all()
    return render(request, 'main.html', {"categories": categories})
