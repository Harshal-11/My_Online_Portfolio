from django.shortcuts import render
from django.http import HttpResponse
from .models import Intro,Gallery
# Create your views here.
def show(request):
    intro_obj = Intro.objects.all()[0]
    gallery_obj = Gallery.objects.all()[0]
    p={'intro':intro_obj,'gallery':gallery_obj}
    return render(request,'about.html',p)