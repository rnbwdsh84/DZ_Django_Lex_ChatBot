from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json

def home(request):
    return render(request, 'home.html')
