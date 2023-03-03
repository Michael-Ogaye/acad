from django.urls import path,include
from .views import stureg,preg,password_reset_request,signin,activate,signout
urlpatterns=[
    
    path('register_student/',stureg,name='stud'),
    path('register_professor/',preg, name='proreg'),
    path("password_reset", password_reset_request, name="password_reset"),
    path('sign_in',signin,name='login'),
    path('activate/<slug:uidb64>/<slug:token>/',  
        activate, name='activate_a'), 
    path('log_out',signout,name='logout'),
     

]
