from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .common import DataDecodification
import datetime

@api_view(["GET", "POST"])
def welcome(request):
    if request.method == 'POST':
        data = request.data
        decoded_data = DataDecodification(data).data_decode()
        if decoded_data != None:
            decoded_data.save()        
            return Response(data)
        else: 
            return Response(status=200)
    else:
        content = {"message": "Welcome to the BookStore!"}
        return JsonResponse(content)
