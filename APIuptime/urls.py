from django import views
from django.urls import path
from . import views


app_name = 'APIuptime'
urlpatterns = [
    path('uptime/', views.uptime, name='uptime'),
]
