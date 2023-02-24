from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=23)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return f'{self.name}---->{self.surname}'
