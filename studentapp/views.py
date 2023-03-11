from django.shortcuts import render,redirect,get_object_or_404
from academicmain.decorotors import student_required
from django.contrib.auth.decorators import login_required
from Authapp.models import Student,Professor
from .models import Task
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from .forms import ProfileEditForm,TaskForm
from django.utils.encoding import force_bytes,force_str

# Create your views here.
@student_required(login_url='login')
def student_home(request):

    contx={}
    uid=urlsafe_base64_encode(force_bytes(request.user.pk))
    latest_tasks=Task.objects.all()[::-1][0:16]
    profs_all=Professor.objects.all()[0:11]
    contx['latest_tasks']=latest_tasks
    contx['profs']=profs_all
    contx['uid']=uid


    return render(request,'studentapp/index.html',contx)



@student_required(login_url='login')
@login_required(login_url='login')
def stud_profile(request, uidb):
    uid=force_str(urlsafe_base64_decode(uidb))
    
    user_profile = get_object_or_404(Student, pk=uid)
    
    
   
    context = {
        'user_prof': user_profile,
        
    }
    
 
    return render(request, 'studentapp/accounts.html', context)


@student_required(login_url='login')
@login_required(login_url='login')
def task(request):
    all_tasks=Task.objects.all()
    uid=urlsafe_base64_encode(force_bytes(request.user.pk))

    return render(request,'studentapp/tasks.html',{'tasks':all_tasks,'uid':uid})




@student_required(login_url='login')
@login_required(login_url='login')
def add_task(request):
    uid=urlsafe_base64_encode(force_bytes(request.user.pk))
    if request.method=='POST':
        form=TaskForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            form=TaskForm(request.POST,request.FILES)
            return render(request,'studentapp/add-task.html',{'form':form,'uid':uid})

    else:
      form=TaskForm()
      return render(request,'studentapp/add-task.html',{'form':form,'uid':uid})
