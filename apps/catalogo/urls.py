from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('gallery/', gallery, name='gallery'),
    path('services/', services, name='services'),
    path('contact/',contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('blogsingle/', blogsingle, name='blogsingle'),
    path ('about/', about, name='about')
]
