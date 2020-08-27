from django.urls import path, include
from .views import dashboard, index, Companies

app_name = 'reports'

urlpatterns = [
    path('', index, name="index"),
    path('dashboard', dashboard, name='dashboard'),
    path('companies', Companies.as_view(), name='companies'),
]