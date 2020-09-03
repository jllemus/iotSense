from django.urls import path, include
from .views import dashboard, index, Companies, AddDevices, Devices

app_name = 'reports'

urlpatterns = [
    path('', index, name="index"),
    path('dashboard', dashboard, name='dashboard'),
    path('companies', Companies.as_view(), name='companies'),
    path('devices', Devices.as_view(), name='devices'),
    path('devices/edit_devices/<str:action>/<str:id>',
         Devices.as_view(), name="edit_device"),
    path('companies/edit_companies/<str:action>/<str:id>', Companies.as_view(), name="edit_company"),
    path('companies/add', Companies.as_view(), name="add_company"),
    path('devices/add', AddDevices.as_view(), name='add_device'),
]
