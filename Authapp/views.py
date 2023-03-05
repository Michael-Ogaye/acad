from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SRegForm,PRegForm,SignForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator as token_g
from  .models import CustomUser,Student,Professor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
# from academicmain.mytoken import account_activation_token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 


from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from .activation import activate_account

def stureg(request):
    if request.method=='POST':
       print('this is rquest.post.....',request.POST)
       form=SRegForm(request.POST)
       if form.is_valid():
          stud= form.save(commit=False)
         
          stud.is_active=False
          
          

          stud.save()
          activate_account(request,stud)
         
          messages.success(request,f'A link has been sent to your email acccount,please confirm your account and log in')
          return redirect('login')
       
       else:
          form=SRegForm(request.POST)
          
          return render(request,'Authapp/registration/studsignup.html',{'form':form})

    else:
       form=SRegForm()
       return render(request,'Authapp/registration/studsignup.html',{'form':form})


def preg(request):
    if request.method=='POST':
       print(request.POST)
       form=PRegForm(request.POST)
       
       if form.is_valid():
          
          pro= form.save(commit=False)
          pro.is_active=False
         
          pro.save()
          activate_account(request,pro)
          messages.success(request,f'A link has been sent to your email acccount,please confirm your account and log in')
          return redirect('login')
       else:
          
          form=SRegForm(request.POST)
          print(form.errors)
          return render(request,'Authapp/registration/profsignup.html',{'form':form})

    else:
       form=SRegForm()
       return render(request,'Authapp/registration/profsignup.html',{'form':form})



def signin(request):
   form=SignForm(initial={})
   if request.method =='POST':
      form=SignForm(request.POST)
      

      
    
      if form.is_valid():
         print('form is valid...first test')
         password=form.cleaned_data.get('password')
         email=form.cleaned_data.get('email')
         user=authenticate(request,username=email,password=password)
         if user is not None and user.is_active:
            login(request,user)
            if user.is_student:
               return HttpResponse('you will be directed to studentapp')
            elif user.is_professor:
               return HttpResponse('you will be directed to the professors page shortly')
            else:
               return HttpResponse('you are being directed to admin page shortly')
         else:
            return HttpResponse('user doesnt exist or you have not activated your account')   
      else:
         form=SignForm()
         print('form is invalid')

         messages.error(request,f'Please make sure you have provided your details in corrrect format')
         return render(request,'Authapp/registration/login.html',{'form':form})
   else:
       form=SignForm()
       return render(request,'Authapp/registration/login.html',{'form':form})
   




def activate(request, uidb64, token):  
    from .models import CustomUser
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))

        user = CustomUser.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):  
        user = None  
   
    
    print(token_g.check_token(user, token))
    if user is not None and token_g.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('login')
    else:  
        return HttpResponse('Activation link is invalid!')  





def password_reset_request(request):
      if request.method == "POST":
         password_reset_form = PasswordResetForm(request.POST)
         if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = CustomUser.objects.filter(Q(email=data))
            if associated_users.exists():
               for user in associated_users:
                  subject = "Password Reset Requested"
                  email_template_name = "Authapp/password_reset_email.txt"
                  c = {
                  "email":user.email,
                  'domain':get_current_site(request).domain,
                  'site_name': 'Feisal',
                  "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                  "user": user,
                  'token': token_g.make_token(user),
                  'protocol': 'http',
                  }
                  email = render_to_string(email_template_name, c)
                  try:
                     send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=True)
                  except BadHeaderError:
                     return HttpResponse('Invalid header found.')
                  return redirect ("password_reset_done")
      password_reset_form = PasswordResetForm()
  
 
 
      return render(request=request, template_name="Authapp/password_reset.html", context={"password_reset_form":password_reset_form})  
@login_required(login_url='login')
def signout(request):
   logout(request)
   return redirect('login')
    
