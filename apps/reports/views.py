from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Device
import requests
# Create your views here.


def index(request):
    return render(request, 'reports/index.html')

# @method_decorator(login_required) Used on class based views
@login_required
def dashboard(request):
    devices_data = Device.objects.all()
    data = {'data': devices_data}
    return render(request, 'reports/dashboard.html', data)