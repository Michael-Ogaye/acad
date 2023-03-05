from django.contrib import admin
from .models import Job,ProfessorProfile

# Register your models here.


class ProfessorprofileAdmin(admin.ModelAdmin):
    list_display=('professor','first_name','lastname','location',)
    list_per_page=30
    list_filter = ('first_name',)
    search_fields = ('first_name',)
   
admin.site.register(ProfessorProfile,ProfessorprofileAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display=('task','belong_to','given_to','has_been_paid','is_complete')
    list_per_page=30
   
admin.site.register(Job,JobAdmin)


