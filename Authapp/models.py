from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator






class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    use_in_migrations = True

    def create_user(self , email ,username, password = None,**extra_fields):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
          
        user = self.model(
            email = self.normalize_email(email) ,
           
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
      
    def create_superuser(self , email , username,password,**extra_fields):
        user = self.create_user(
            email = self.normalize_email(email) ,
            password = password,
            username=username,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
     class Types(models.TextChoices):
        STUDENT = "STUDENT" , "student"
        PROFESSOR = "PROFESSOR" , "professor"
        C_ADMIN='C_ADMIN','c_admin'
    
    # r'^\+?1?\d{9,15}$'

     phone_regex = RegexValidator(regex=r'^\+?\d{1,3}-\d{6,15}$',
                                 message="Phone number must be entered in the format: '+1-578954324'. Up to 15 digits allowed.")     
     type = models.CharField(max_length = 40 , choices = Types.choices , 
                            # Default is user is teacher
                            default = Types.C_ADMIN)
     email = models.EmailField(max_length = 200 , unique = True)
    #  phone_number=models.CharField(max_length=65,unique=True)
     username=models.CharField(max_length=30,null=True)
     password=models.CharField(max_length=100)
     date_joined=models.DateTimeField(auto_now_add=True,max_length=100)
     is_active = models.BooleanField(default = True)
     is_admin = models.BooleanField(default = False)
     is_staff = models.BooleanField(default = False)
     is_superuser = models.BooleanField(default = False)

     is_student = models.BooleanField(default = False)
     is_professor = models.BooleanField(default = False)
     is_c_admin=models.BooleanField(default=False)
    
     USERNAME_FIELD='email'
     REQUIRED_FIELDS=('phone_number','username',)
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
    def create_user(self , email ,username, password = None,**extra_fields):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(
            email = email,
            username=username,
            **extra_fields
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
    def create_user(self , email ,username, password = None,**extra_fields):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email = email.lower()
        user = self.model(
            email = email,
            username=username,
            **extra_fields
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
    def create_user(self , email ,username, password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email = email.lower()
        user = self.model(
            email = email,
            username=username
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
