from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from createbooking.models import bookingmodel

# Create your views here.

def booking(request):
    if request.method == "POST":
        name = request.POST.get('name') 
        start = request.POST.get('start')
        end = request.POST.get('end')

        print(name, start, end)

        newitem = bookingmodel(name=request.POST.get('name'), start=start, end=end)
        newitem.save()

        return HttpResponseRedirect(reverse('createbooking:overview'))

    else:
        return render(request, 'main.html')