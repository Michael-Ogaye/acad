from django.urls import path
from .views  import student_home,task,stud_profile,add_task


urlpatterns=[
    path('',student_home,name='stud_home'),
    path('all_tasks/',task,name='tasks'),
    path('profile/<slug:uidb>/',stud_profile,name='stud_prof'),
    path('add_task',add_task,name='add-task'),
    
]