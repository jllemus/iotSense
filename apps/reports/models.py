from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_id = models.CharField(max_length=200, default="0000")
    company_location = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, default='None')

    def __str__(self):
        return self.user.username


class SensorType(models.Model):
    variable_name = models.CharField(max_length=300)
    variable_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.variable_name

class Device(models.Model):
    device_name = models.CharField(max_length=200)
    device_mac = models.CharField(max_length=200)
    device_id = models.CharField(max_length=200, default="0000")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        title = '%s | %s' %(self.device_id, self.device_name)
        return title

class DeviceInfo(models.Model):
    device_data = models.CharField(max_length=1000)
    device = models.OneToOneField(Device, on_delete=models.CASCADE)


