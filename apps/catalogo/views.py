from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    allservicios = servicios.objects.all()
    return render(request, 'index.html', {'allservicios':allservicios})

def gallery(request):
    return render(request, 'gallery.html')

def services(request):
    allservicios = servicios.objects.all()
    return render(request, 'services.html', {'allservicios': allservicios})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blogsingle(request):
    return render(request, 'blog-single.html')