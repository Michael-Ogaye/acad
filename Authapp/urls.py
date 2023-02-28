from django.urls import path,include
from .views import stureg,preg,password_reset_request,signin
urlpatterns=[
    
    path('register_student/',stureg,name='stud'),
    path('register_professor/',preg, name='proreg'),
    path("password_reset", password_reset_request, name="password_reset"),
    path('sign_in',signin,name='login'),
    # path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
    #     activate, name='activate'), 
    # 
     

]
