from django.urls import path

from . import views

app_name = "viewbooking"

urlpatterns = [
    path('', views.viewbooking, name='view'),
]