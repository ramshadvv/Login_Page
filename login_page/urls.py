from importlib.resources import path
from django.urls import path
from .views import home, user_login, user_logout

urlpatterns = [
    path('',user_login, name="user_login"),
    path('home',home, name='home'),
    path('logout',user_logout, name='logout'),
]