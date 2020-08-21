from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.


def index(request):
    return render(request, 'reports/index.html')


def dashboard(request):
    return render(request, 'reports/dashboard.html')