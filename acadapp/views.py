from django.shortcuts import render,redirect

from .models import Subscriber
from .email import sendEmail
from django.contrib import messages

# Create your views here.

def home(request):
   if request.method=='POST':
        name=request.POST.get('name')
        surname=request.POST.get('surname')
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        subscriber= Subscriber.objects.create(name=name,surname=surname,email=email,subject=subject,message=message)
        subscriber.save()
        messages.success(request,f'Thank you {name} for choosing to talk to us')
        sendEmail(request,[email,])
        return redirect('hm')

        
   else:
        return render(request,'acadapp/index.html')


def real(request):
    return render(request,'acadapp/realt.html')

