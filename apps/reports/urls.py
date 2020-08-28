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
    path('devices/addDevice', AddDevices.as_view(), name='add_device'),
]
