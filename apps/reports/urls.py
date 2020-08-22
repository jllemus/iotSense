from django.urls import path
from .views import dashboard, index

app_name = 'reports'

urlpatterns = [
    path('', index, name="reports_index"),
    path('dashboard', dashboard, name='reports_dashboard'),
]