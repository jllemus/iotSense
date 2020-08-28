from django.forms import ModelForm
from .models import Device


class AddDeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
