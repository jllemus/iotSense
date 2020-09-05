# {
#     'geolocSource': 2,
#     'device_id': 'D09469',
#     'lng': -74.79780401883814,
#     '_raw': {
#         'duplicates': [{'bsId': '677F', 'rssi': -132, 'nbRep': 2, 'snr': 6.6}],
#         'deviceTypeId': '5e0179e02564324b86fa1d9e',
#         'fixedLat': '0.0',
#         'data': '0201',
#         'lqi': 'Limit',
#         'countryCode': '170',
#         'fixedLng': '0.0',
#         'seqNumber': '543',
#         'time': '1598742742',
#         'computedLocation': {
#             'lng': -74.79780401883814,
#             'source': 2,
#             'radius': 16100,
#             'lat': 10.922418368478585,
#             'status': 1
#         },
#             'device': 'D09469',
#             'operatorName': 'SIGFOX_Colombia_Phaxsi'
#     },
#         'radius': 16100,
#         'lat': 10.922418368478585,
#         'timestamp': '1598742742'
# }

# TYPE DICT
# LEN 7

# ANOTHER TYPE OF MESSAGE
# {
#     'mode': '2',
#     'device_name': 'Beacon',
#     'hw_version': '5.4',
#     'data': '0201',
#     'device_id': 'D09469',
#     '_raw': {
#         'rssi': '-132.00',
#         'data': '0201',
#         'lng': 'null',
#         'ack': 'false',
#         'duplicate': 'null',
#         'avgSnr': 'null',
#         'longPolling': 'false',
#         'snr': '6.78',
#         'station': '677F',
#         'seqNumber': '547',
#         'time': '1598743023',
#         'device': 'D09469',
#         'lat': 'null'
#     },
#     'state': 'moved',
#     'fw_version': '1.7',
#     'timestamp': 1598743023,
#     'lng': 'null',
#     'lat': 'null',
#     'status_battery': 'MEDIUM',
#     'status_voltage': '2.719'
# }

# TYPE DICT
# LEN 13
from apps.reports.models import Device, DeviceInfo
import datetime
import json


class DataDecodification:
    def __init__(self, data):
        self.data = data

    def data_decode(self):
        '''Checks which type of device is sendind data'''
        try:
            device_name = self.data['device_name']
            if device_name == 'Sense' or device_name == 'Beacon':
                decoded_data = self.unabiz_decode(self.data)
                return decoded_data
        except:
            return None

    def unabiz_decode(self, data):
        decoded_data = {}
        device_name = data['device_name']
        if device_name == 'Beacon':
            decoded_data["device_brand"] = 'unabiz'
            decoded_data["device_name"] = data['device_name']
            decoded_data["device_id"] = Device.objects.get(
                device_id=data['device_id'])
            decoded_data["device_state"] = data['state']
            decoded_data["temperature"] = 'N/A'
            decoded_data["humidity"] = 'N/A'
            device_info = DeviceInfo(state=decoded_data['device_state'], timestamp=datetime.datetime.now(
            ), device=decoded_data['device_id'])
        elif device_name == 'Sense':
            decoded_data["device_brand"] = 'unabiz'
            decoded_data["device_name"] = data['device_name']
            decoded_data["device_id"] = Device.objects.get(
                device_id=data['device_id'])
            decoded_data["temperature"] = data['temperature']
            decoded_data["humidity"] = data['humidity']
            decoded_data["device_state"] = 'N/A'
            device_info = DeviceInfo(humidity=decoded_data['humidity'], temperature=decoded_data['temperature'],
                                     timestamp=datetime.datetime.now(), device=decoded_data['device_id'])
        return device_info
