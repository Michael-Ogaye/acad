from django.urls import path
from .views import home,real

urlpatterns=[
    path('',home, name='hm'),
    path('second',real,name='real'),
    

]