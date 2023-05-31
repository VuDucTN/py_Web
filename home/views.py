from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Contact
# Create your views here.
def index(request): 
    return render(request,'pages/home.html')
def contact(request):
    if request.method == 'POST':
        contactSend = Contact()
        contactSend.username = request.POST['username']
        contactSend.email = request.POST['email']
        contactSend.phone = request.POST['phone']
        contactSend.message = request.POST['message']

        contactSend.save()
        return redirect('/contact/')
    return render(request, 'pages/contact.html')
def about(request):
    return render(request, 'pages/about.html')
@login_required
def profile(request):
    return render(request, 'pages/profile.html')
def error_404(request, exception):
   return render(request,'pages/error_404.html')
def error_500(request):
   context = {}
   return render(request,'', context)

