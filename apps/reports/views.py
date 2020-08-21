from django.shortcuts import render
from django.http import HttpResponse
from .models import Device
import requests
# Create your views here.


def index(request):
    return render(request, 'reports/index.html')


def dashboard(request):
    devices_data = Device.objects.all()
    data = {'data': devices_data}
    return render(request, 'reports/dashboard.html', data)