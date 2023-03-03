from django.db import models
from Authapp.models import Cadmin

from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

class AdminProfile(models.Model):
    admin=models.OneToOneField(Cadmin,on_delete=models.CASCADE,related_name='profile')
    first_name=models.CharField(max_length=30,blank=True,null=True)
    surname=models.CharField(max_length=30,blank=True,null=True)
    lastname=models.CharField(max_length=30,blank=True,null=True)
    profile_picture =CloudinaryField('admin_images',blank=True,null=True)
    location=models.CharField(max_length=90,blank=True)
    

    def __str__(self):
        return f'{self.admin.username} Profile'

    @receiver(post_save, sender=Cadmin)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            AdminProfile.objects.create(student=instance)

    @receiver(post_save, sender=Cadmin)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.admin.profile.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(Cadmin__username__icontains=name).all()


# Create your models here.
