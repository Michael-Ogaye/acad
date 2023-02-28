from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SRegForm,PRegForm,SignForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate,login,logout
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from  .models import CustomUser,Student,Professor

from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
# from academicmain.mytoken import account_activation_token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 


from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm

def stureg(request):
    if request.method=='POST':
       print('this is rquest.post.....',request.POST)
       form=SRegForm(request.POST)
       if form.is_valid():
          stud= form.save(commit=False)

          stud.password =make_password(form.cleaned_data['password'])
          stud.is_active=True
          stud.save()
          current_site = get_current_site(request)  

         #  cntx_em={  
         #        'user': stud,  
         #        'domain': current_site.domain,  
         #        'uid':urlsafe_base64_encode(force_bytes(stud.pk)),  
         #        'token':account_activation_token.make_token(stud),  
         #    }
          messages.success(request,f'A link has been sent to your email acccount,please confirm your account and log in')
          return HttpResponse('succesfully registered')

    else:
       form=SRegForm()
       return render(request,'Authapp/registration/studsignup.html',{'form':form})


def preg(request):
    if request.method =='POST':
       print(request.POST)
       form=PRegForm(request.POST)
       if form.is_valid():
          
          pro= form.save(commit=False)

          pro.password =make_password(form.cleaned_data['password'])
          pro.is_active=False
          pro.save()
          messages.success(request,f'A link has been sent to your email acccount,please confirm your account and log in')
          return HttpResponse('succesfully registered')
       else:
          
          form=SRegForm()
          return render(request,'Authapp/registration/profsignup.html',{'form':form})

    else:
       form=SRegForm()
       return render(request,'Authapp/registration/profsignup.html',{'form':form})



def signin(request):
   if request.method=='POST':
      form=SignForm(request.POST)
    
      if form.is_valid():
         print('form is valid...first test')
         password=form.cleaned_data.get('password')
         email=form.cleaned_data.get('email')
         user=authenticate(request,email=email,password=password)
         if user is not None:
            login(request,user)
            if user.is_student:
               return HttpResponse('you will be directed to studentapp')
            elif user.is_professor:
               return HttpResponse('you will be directed to the professors page shortly')
            else:
               return HttpResponse('you are being directed to admin page shortly')
         else:
            return HttpResponse('user doesnt exist')   
      else:
         form=SignForm()
         print('form is invalid')

         messages.error(request,f'Please make sure you have provided your details in corrrect format')
         return render(request,'Authapp/registration/login.html',{'form':form})
   else:
       form=SignForm()
       return render(request,'Authapp/registration/login.html',{'form':form})
   



# def activate(request, uidb64, token):  
#     User = get_user_model()  
#     try:  
#         uid = force_text(urlsafe_base64_decode(uidb64))  
#         user = User.objects.get(pk=uid)  
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
#         user = None  
#     if user is not None and account_activation_token.check_token(user, token):  
#         user.is_active = True  
#         user.save()  
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
#     else:  
#         return HttpResponse('Activation link is invalid!')  





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
                  'site_name': 'Benbrands',
                  "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                  "user": user,
                  'token': default_token_generator.make_token(user),
                  'protocol': 'http',
                  }
                  email = render_to_string(email_template_name, c)
                  try:
                     send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=True)
                  except BadHeaderError:
                     return HttpResponse('Invalid header found.')
                  return redirect ("/password_reset/done/")
      password_reset_form = PasswordResetForm()
      return render(request=request, template_name="Authapp/password_reset.html", context={"password_reset_form":password_reset_form})   