from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def welcome(request):
    if request.method == 'POST':
        data = request.data
        return Response(data)
    else:
        content = {"message": "Welcome to the BookStore!"}
        return JsonResponse(content)
