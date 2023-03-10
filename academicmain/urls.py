"""academicmain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views #import this


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('acadapp.urls')),
    path('account/',include('Authapp.urls')),
    # path('account_default/', include('django.contrib.auth.urls')),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Authapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="Authapp/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Authapp/password_reset_complete.html'), name='password_reset_complete'), 
    path('student/',include('studentapp.urls')) ,
    path('professor/',include('professorapp.urls')) , 
    path('feasal_admin/',include('adminapp.urls')),

]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)