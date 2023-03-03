from django.shortcuts import render
from academicmain.decorotors import student_required

# Create your views here.
@student_required(login_url='login')
def student_home(request):
    return render(request,'studentapp/student_home.html')
