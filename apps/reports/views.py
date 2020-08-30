from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Device, Profile, Company
from .common import DataDecodification
from .forms import AddDeviceForm
import requests
# Create your views here.




def index(request):
    data = {'mode': '2', 'device_name': 'Beacon', 'hw_version': '5.4', 'data': '0201', 'device_id': 'D09469', '_raw': {'rssi': '-132.00', 'data': '0201', 'lng': 'null', 'ack': 'false', 'duplicate': 'null', 'avgSnr': 'null', 'longPolling': 'false', 'snr': '6.78',
                                                                                                                   'station': '677F', 'seqNumber': '547', 'time': '1598743023', 'device': 'D09469', 'lat': 'null'}, 'state': 'moved', 'fw_version': '1.7', 'timestamp': 1598743023, 'lng': 'null', 'lat': 'null', 'status_battery': 'MEDIUM', 'status_voltage': '2.719'}
    decoded_data = DataDecodification(data).data_decode()
    print(decoded_data)
    return render(request, 'reports/index.html')

# @method_decorator(login_required) Used on class based views
@login_required
def dashboard(request):
    user = request.user
    data = validation_superuser(user, Device, Company)
    return render(request, 'reports/dashboard.html', {'devices': data, 'device_number': data.count()})


@method_decorator(login_required, name='get')
# @method_decorator(user_passes_test(lambda u: u.is_superuser), name='get')
class Companies(TemplateView):
    template_name = "reports/companies.html"

    def get(self, request):
        try:
            company_data = {}
            companies_objects = Company.objects.all()
            for company in companies_objects:
                number_devices = Device.objects.filter(
                    company=company).count()
                company_data[company.company_name] = [company.company_id,
                                                      company.company_location,
                                                      number_devices]
            return render(request, self.template_name, {'company_data': company_data})
        except:
            return HttpResponse('<h1> You don\'t have permission to access this page </h1>', status=400)


@method_decorator(login_required, name='get')
class Devices(TemplateView):
    template_name = 'reports/devices.html'

    def get(self, request):
        user = request.user
        devices = validation_superuser(user, Device, Company)
        return render(request, self.template_name, {'devices': devices})

    def post(self, request, action, id):
        print("here")
        if action == 'delete':
            obj = get_object_or_404(Device, pk=int(id))
            obj.delete()
            return redirect('reports:devices')
        

@method_decorator(login_required, name="get")
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='get')
class AddDevices(TemplateView):
    template_name = "reports/add_device.html"

    def get(self, request):
        user = request.user
        if user.is_superuser:
            form = AddDeviceForm()
            print(form)
            return render(request, self.template_name, {'form': form})
        else:
            raise 404
    
    def post(self, request):
        data = request.POST 
        form_filled = AddDeviceForm(data)
        if form_filled.is_valid():
            form_filled.save()
            return redirect("reports:devices")

def validation_superuser(user, *model):
    if user.is_superuser:
        devices = model[0].objects.all()
    else:
        company = model[1].objects.get(id=user.id)
        devices = model[0].objects.filter(company=company)
    return devices
