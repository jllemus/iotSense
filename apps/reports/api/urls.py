from django.urls import path, include
from apps.reports.api.views import welcome

app_name = 'reports'

urlpatterns = [
    ## REST DJANGO API
    path('', welcome, name="reports_api"),
]