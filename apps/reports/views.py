from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Device, Profile, Company
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


@method_decorator(login_required, name='get')
# @method_decorator(user_passes_test(lambda u: u.is_superuser), name='get')
class Companies(TemplateView):
    template_name = "reports/companies.html"

    def get(self, request):
        user = request.user
        try:
            if user.is_superuser:
                company_data = {}
                companies_objects = Company.objects.all()
                for company in companies_objects:
                    number_devices = Device.objects.filter(company=company).count()
                    company_data[company.company_name] = [company.company_id,
                                                        company.company_location,
                                                        number_devices]
                return render(request, self.template_name, {'company_data':company_data})
        except:
            return HttpResponse('<h1> You don\'t have permission to access this page </h1>', status=400)
