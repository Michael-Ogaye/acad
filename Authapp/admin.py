from django.contrib import admin
from .models import CustomUser,Professor,Cadmin


admin.site.register(CustomUser)
admin.site.register(Professor)
admin.site.register(Cadmin)
# Register your models here.
