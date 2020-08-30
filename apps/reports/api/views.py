from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DeviceInfoSerializer

@api_view(["GET", "POST"])
def welcome(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        print(type(data))
        print(len(data))
        ##DESERIALIZATION 
        # new_data = JSONParser().parse(decoded_data)
        # deserialized_data = DeviceInfoSerializer(data=decoded_data)
        # if deserialized_data.is_valid():
        #     deserialized_data.save()
        #     return JsonResponse(deserialized_data, status=201)

        return Response(data)
    else:
        content = {"message": "Welcome to the BookStore!"}
        return JsonResponse(content)
