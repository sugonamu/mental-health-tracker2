from django.urls import path
from authetication.views import login, register, logout


app_name = 'authetication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]