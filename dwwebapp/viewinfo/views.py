from django.shortcuts import render
from createbooking.models import bookingmodel

# Create your views here.

def viewbooking(request):
    data = bookingmodel.objects.all()
    return render(request, "view.html", {'data':data})