from django.urls import path

from . import views

app_name = "createbooking"

urlpatterns = [
    path('', views.booking, name='overview'),
]