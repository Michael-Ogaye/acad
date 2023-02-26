from django.shortcuts import render
from django.http import HttpResponse
from .forms import SRegForm,PRegForm
from django.contrib import messages
# Create your views here.

def stureg(request):
    if request.method=='POST':
       form=SRegForm(request.POST)
       if form.is_valid():
          stud= form.save(commit=False)
          stud.is_active=False
          stud.save()
          messages.success(request,f'A link has been sent to your email acccount,please confirm your account and log in')
          return HttpResponse('succesfully registered')

    else:
       form=SRegForm()
       return render(request,'Authapp/registration/studsignup.html',{'form':form})


def preg(request):
    if request.method=='POST':
       form=PRegForm(request.POST)
       if form.is_valid():
          stud= form.save(commit=False)
          stud.is_active=False
          stud.save()
          messages.success(request,f'A link has been sent to your email acccount,please confirm your account and log in')
          return HttpResponse('succesfully registered')

    else:
       form=SRegForm()
       return render(request,'Authapp/registration/profsignup.html',{'form':form})

