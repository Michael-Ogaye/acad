from django.contrib import admin
from .models import CustomUser,Professor,Cadmin,Student


admin.site.register(CustomUser)
admin.site.register(Professor)
admin.site.register(Cadmin)
admin.site.register(Student)
# Register your models here.
