from django.contrib import admin
from .models import StudentProfile,Task,TaskCategory,StudentReview

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(Task)
admin.site.register(TaskCategory)
