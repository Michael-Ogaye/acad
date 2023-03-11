from django.db import models
from django.contrib.auth import get_user_model
from Authapp.models import Student


from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

class StudentProfile(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE,related_name='stud_profile')
    first_name=models.CharField(max_length=30,blank=True,null=True)
    surname=models.CharField(max_length=30,blank=True,null=True)
    lastname=models.CharField(max_length=30,blank=True,null=True)
    profile_picture =CloudinaryField('student_images',blank=True,null=True,resource_type="auto")
    location=models.CharField(max_length=90,blank=True)
    

    def __str__(self):
        return f'{self.student.username} Profile'

    @receiver(post_save, sender=Student)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            StudentProfile.objects.create(student=instance)

    @receiver(post_save, sender=Student)
    def save_user_profile(sender, instance, **kwargs):
        instance.stud_profile.save()

    def save_profile(self):
        pass

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(Student__username__icontains=name).all()



class TaskCategory(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()


    class Meta:
     verbose_name_plural = "categories"

    def __str__(self):
       return f'category--{self.name}'




class Task(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    files=CloudinaryField('task_files', blank=True,null=True,resource_type='auto')
    task_url=models.URLField(blank=True,null=True)
    deadline_date = models.DateTimeField('Task Deadline Date')
    created_at = models.DateTimeField(auto_now_add=True)
    bid_amount=models.DecimalField(max_digits=7,decimal_places=2)
    stud=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='tasks')
    category=models.ForeignKey(TaskCategory,on_delete=models.SET_NULL,null=True,blank=True)
    is_pending=models.BooleanField(default=True)
    is_complete=models.BooleanField(default=False)
    

    

    def __str__(self):
     return str(self.name) 

    class Meta:
     verbose_name_plural = "Tasks"
     


class StudentReview(models.Model):
   pass
#    job=models.ManyToManyField(Job,related_name='stud_review')
#    review=models.TextField()
   

# Create your models here.


