from django.contrib import admin
from apps.reports.models import Company, Device, SensorType, DeviceInfo, Profile
# Register your models here.

admin.site.register(Company)
admin.site.register(Device)
admin.site.register(SensorType)
admin.site.register(DeviceInfo)
admin.site.register(Profile)