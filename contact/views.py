from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import ContactForm
# Create your views here.
def dis(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        m = request.POST.get('message')
        current_date = date.today()
        contact_entry = ContactForm(name=n,email=e,message=m,post_date=current_date)
        contact_entry.save()
        return render(request,'contact.html',{'res':'done'})
    return render(request,'contact.html')