from django.db import models
from Authapp.models import Professor,Student
from studentapp.models import Task

# Create your models here.

from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

class ProfessorProfile(models.Model):
    professor=models.OneToOneField(Professor,on_delete=models.CASCADE,related_name='pro_profile')
    first_name=models.CharField(max_length=30,blank=True,null=True)
    surname=models.CharField(max_length=30,blank=True,null=True)
    lastname=models.CharField(max_length=30,blank=True,null=True)
    profile_picture =CloudinaryField('professor_images',blank=True,null=True)
    location=models.CharField(max_length=90,blank=True)
    

    def __str__(self):
        return f'{self.professor.username} Profile'

    @receiver(post_save, sender=Professor)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ProfessorProfile.objects.create(professor=instance)

    @receiver(post_save, sender=Professor)
    def save_user_profile(sender, instance, **kwargs):
        instance.pro_profile.save()

    def save_profile(self):
        self.professor.pro_profile.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(Professor__username__icontains=name).all()



class Bid (models.Model):
    bided_by=models.ManyToManyField(Professor)
    task=models.ManyToManyField(Task,related_name='bids')
    amount=models.DecimalField(max_digits=7,decimal_places=2)
    bid_date=models.DateTimeField(auto_now_add=True)
    accepted=models.BooleanField(default=False)
    rejected=models.BooleanField(default=False)

class Job(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    belong_to=models.ForeignKey(Student,related_name='Student_jobs',on_delete=models.CASCADE)
    given_at=models.DateTimeField(auto_now_add=True)

    given_to=models.ForeignKey(Professor,related_name='jobs',on_delete=models.CASCADE)
    is_complete=models.BooleanField(default=False)
    has_been_paid=models.BooleanField(default=False)