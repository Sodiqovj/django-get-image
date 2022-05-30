from django.shortcuts import render
from .models import Car, Imgs

def home(request):
    images = Imgs.objects.all()
    connect = Car.objects.all()
    context = {
        "view": connect,
        "image":images
    }
    return render(request, 'index.html', context)
