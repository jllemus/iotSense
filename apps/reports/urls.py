from django.urls import path, include
from .views import dashboard, index

app_name = 'reports'

urlpatterns = [
    path('', index, name="index"),
    path('dashboard', dashboard, name='dashboard'),
]