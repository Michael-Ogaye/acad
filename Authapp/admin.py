from django.contrib import admin
from .models import CustomUser,Professor,Cadmin,Student


class CutomUserAdmin(admin.ModelAdmin):
    list_display=('email','phone_number','username','date_joined',)
    list_filter = ('username',)
    search_fields = ('username',)
    list_display_links = ('email',)
    list_per_page=30

admin.site.register(CustomUser,CutomUserAdmin)


class ProfAdmin(admin.ModelAdmin):
    list_display=('email','phone_number','username','date_joined',)
    list_per_page=30
    list_filter = ('username',)
    search_fields = ('username',)
    list_display_links = ('email',)
admin.site.register(Professor,ProfAdmin)  

class CadAdmin(admin.ModelAdmin):
    list_display=('email','phone_number','username','date_joined',)
    list_per_page=30
    list_filter = ('username',)
    search_fields = ('username',)
    list_display_links = ('email',)
admin.site.register(Cadmin,CadAdmin)

class StudAdmin(admin.ModelAdmin):
    list_display=('email','phone_number','username','date_joined',)
    list_per_page=30
    list_filter = ('username',)
    search_fields = ('username',)
    list_display_links = ('email',)
admin.site.register(Student,StudAdmin)
# Register your models here.
