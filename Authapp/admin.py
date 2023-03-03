from django.contrib import admin
from .models import CustomUser,Professor,Cadmin,Student


class CutomUserAdmin(admin.ModelAdmin):
    list_display=('email','phone_number','username')
    list_per_page=30

admin.site.register(CustomUser)


class ProfAdmin(admin.ModelAdmin):
    list_display=('email','phone_number','username')
    list_per_page=30
admin.site.register(Professor)  

class CadAdmin(admin.ModelAdmin):
    list_display=('email','phone_number','username')
    list_per_page=30
admin.site.register(Cadmin)

class StudAdmin(admin.ModelAdmin):
    list_display=('email','phone_number','username')
    list_per_page=30
admin.site.register(Student)
# Register your models here.
