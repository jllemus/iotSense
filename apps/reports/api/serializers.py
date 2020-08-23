from rest_framework import serializers
from ..models import DeviceInfo

class DeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo