from django.urls import path,include
from .views import stureg,preg
urlpatterns=[
    
    path('register_student/',stureg,name='stud'),
    path('register_professor/',preg, name='proreg'),
]
