from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_id = models.IntegerField()
    company_location = models.CharField(max_length=200)

class Device(models.Model):
    device_name = models.CharField(max_length=200)
    device_mac = models.CharField(max_length=200)
    device_id = models.IntegerField()
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)

