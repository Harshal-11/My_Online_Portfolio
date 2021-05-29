from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero,Testimonial
# Create your views here.

def display(request): 
    hero_obj = Hero.objects.all()[0]
    testimonial_obj = Testimonial.objects.all()
    param = {'hero':hero_obj,'testimonial':testimonial_obj}
    return render(request,'home.html',param)