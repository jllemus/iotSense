from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Device, Profile, Company, DeviceInfo
from .forms import AddDeviceForm
from django.utils import timezone


def index(request):
    return render(request, 'reports/index.html')

# @method_decorator(login_required) Used on class based views
@login_required
def dashboard(request):
    user = request.user
    devices, devices_info = validation_superuser(user)
    try:
        devices_info = devices_info.order_by('-timestamp')
        online_devices, offline_devices = active_devices(devices)
        data = {
            'devices': devices,
            'devices_info': devices_info,
            'online': online_devices,
            'offline': offline_devices
        }
    except:
        data = {
            'devices': devices,
            'devices_info': devices_info,
            'online': 0,
            'offline': 0
        }

    return render(request, 'reports/dashboard.html', data)


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
                company_data[company.company_name] = [company, number_devices]
            return render(request, self.template_name, {'company_data': company_data})
        except:
            return HttpResponse('<h1> You don\'t have permission to access this page </h1>', status=400)

    def post(self, request, action, id):
        delete(Company, action, id)
        return redirect('reports:companies')

@method_decorator(login_required, name='get')
class Devices(TemplateView):
    template_name = 'reports/devices.html'

    def get(self, request):
        devices_dict = {}
        user = request.user
        devices, _ = validation_superuser(user)
        try:
            for device in devices:
                device_info = DeviceInfo.objects.filter(
                    device=device).order_by('-timestamp')
                devices_dict[device.device_name] = [device, device_info]
        except:
            devices_dict = {}
        return render(request, self.template_name, {'devices_dict': devices_dict})

    def post(self, request, action, id):
        delete(Device, action, id)
        return redirect('reports:devices')

@method_decorator(login_required, name="get")
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='get')
class AddDevices(TemplateView):
    template_name = "reports/add_device.html"

    def get(self, request):
        user = request.user
        if user.is_superuser:
            form = AddDeviceForm()
            return render(request, self.template_name, {'form': form})
        else:
            raise 404

    def post(self, request):
        data = request.POST
        form_filled = AddDeviceForm(data)
        if form_filled.is_valid():
            form_filled.save()
            return redirect("reports:devices")

def validation_superuser(user):
    if user.is_superuser:
        devices = Device.objects.all()
        devices_info = DeviceInfo.objects.all()
    else:
        devices_info = []
        profile = Profile.objects.get(user=user)
        devices = Device.objects.filter(company=profile.company)
        for device in devices:
            devices_info.append(DeviceInfo.objects.filter(device=device))
    return devices, devices_info

def delete(model, action, id):
    if action == 'delete':
        item = get_object_or_404(model, pk=int(id))
        item.delete()

def active_devices(devices):
    online_devices = 0
    offline_devices = 0
    for device in devices:
        last_device_info = DeviceInfo.objects.filter(device=device).last()
        if last_device_info != None:
            time_difference = timezone.now() - last_device_info.timestamp
            seconds_in_day = 24 * 60 * 60
            time_difference = divmod(
                time_difference.days * seconds_in_day + time_difference.seconds, 60)
            if time_difference[0] < 10:
                online_devices += 1
            else:
                offline_devices += 1
    return online_devices, offline_devices
