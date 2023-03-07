from django.shortcuts import render,redirect,get_object_or_404
from academicmain.decorotors import student_required
from django.contrib.auth.decorators import login_required
from Authapp.models import Student


# Create your views here.
@student_required(login_url='login')
def student_home(request):
    return render(request,'studentapp/student_home.html')



@student_required(login_url='login')
@login_required(login_url='login')
def stud_profile(request, email):
    user_profile = get_object_or_404(Student, emal=email)
    if request.user == user_profile:
        return redirect('profile', email=request.user.email)
    
    
   
    context = {
        'user_prof': user_profile,
        
    }
    
    return render(request, 'studentapp/stud_profile.html', context)