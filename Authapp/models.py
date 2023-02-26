from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _





class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self , email ,phone_number, password = None,):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
          
        user = self.model(
            email = self.normalize_email(email) ,
            phone_number=phone_number 
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
      
    def create_superuser(self , email , password,phone_number):
        user = self.create_user(
            email = self.normalize_email(email) ,
            phone_number=phone_number,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class CustomUser(AbstractBaseUser):
     class Types(models.TextChoices):
        STUDENT = "STUDENT" , "student"
        PROFESSOR = "PROFESSOR" , "professor"
        C_ADMIN='C_ADMIN','c_admin'
          
     type = models.CharField(max_length = 20 , choices = Types.choices , 
                            # Default is user is teacher
                            default = Types.C_ADMIN)
     email = models.EmailField(max_length = 200 , unique = True)
     phone_number=models.PositiveIntegerField()

     is_active = models.BooleanField(default = True)
     is_admin = models.BooleanField(default = False)
     is_staff = models.BooleanField(default = False)
     is_superuser = models.BooleanField(default = False)

     is_student = models.BooleanField(default = False)
     is_professor = models.BooleanField(default = False)
     is_c_admin=models.BooleanField(default=False)

     USERNAME_FIELD='email'
     REQUIRED_FIELDS=('phone_number',)
     objects=CustomUserManager()

     def __str__(self):
        return str(self.email)
      
     def has_perm(self , perm, obj = None):
        return self.is_admin
      
     def has_module_perms(self , app_label):
        return True

     def save(self , *args , **kwargs):
        if not self.type or self.type == None : 
            self.type = CustomUser.Types.C_ADMIN
        return super().save(*args , **kwargs)
     


class StudentManager(models.Manager):
    def create_user(self , email , password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
      
    def get_queryset(self , *args,  **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = CustomUser.Types.STUDENT)
        return queryset  

class Student(CustomUser):

    class Meta:
        proxy=True
    objects=StudentManager()

    def save(self , *args , **kwargs):
        self.type = CustomUser.Types.STUDENT
        self.is_student = True
        return super().save(*args , **kwargs)



class ProfessorManager(models.Manager):
    def create_user(self , email , password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email = email.lower()
        user = self.model(
            email = email
        )
        user.set_password(password)
        
        user.save(using = self._db)
        return user
        
    def get_queryset(self , *args , **kwargs):

        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = CustomUser.Types.PROFESSOR)
        return queryset
    

      
class Professor(CustomUser):

    
    
    class Meta :
        proxy = True
    objects = ProfessorManager()
      
    def save(self  , *args , **kwargs):
        self.type = CustomUser.Types.PROFESSOR
        self.is_professor = True
        return super().save(*args , **kwargs)



class CadminManager(models.Manager):
    def create_user(self , email , password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email = email.lower()
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
        
    def get_queryset(self , *args , **kwargs):

        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = CustomUser.Types.C_ADMIN)
        return queryset
    

      
class Cadmin(CustomUser):
    class Meta :
        proxy = True
    objects = CadminManager()
      
    def save(self  , *args , **kwargs):
        self.type = CustomUser.Types.C_ADMIN
        self.is_c_admin = True
        return super().save(*args , **kwargs)

# Create your models here.
