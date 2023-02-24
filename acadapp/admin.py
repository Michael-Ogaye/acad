from django.contrib import admin
from .views import Subscriber

admin.site.register(Subscriber)

# class SubscriberAdmin(admin.ModelAdmin):
#     list_display=('name','surname')
    
# Register your models here.
