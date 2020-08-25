from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="user_login"),
    path('logout/', LogoutView.as_view(), name='user_logout'),
]