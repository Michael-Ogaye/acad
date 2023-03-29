from .models import Cadmin,CustomUser,Professor,Student
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()

class SRegForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        'username_required': ("username field is required"),
        'phone_required':("Phone number is required"),
        'password_required':("Password must have minimum of 5 characters"),
        'email_required':("email is required")
    }
    password1 = forms.CharField(label=("Password"),
                              widget=forms.PasswordInput)
 

    class Meta:
     model = Student
     fields = [ 'email','username','password']


    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password and password1 and password != password1:
          raise forms.ValidationError(
            self.error_messages['password_mismatch'],
            code='password_mismatch',
        )
        return password1

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username)==0:
            raise forms.ValidationError(
                self.error_messages['username_required'],
                code='username_required'
            )
        return username
    
    def clean_email(self):
        email= self.cleaned_data.get('email')
        if  len(email)==0:
            raise forms.ValidationError(
                self.error_messages['email_required'],
                code='email_required'
            )
        if '@' not in email:
            raise forms.ValidationError('That is not a valid email address ',code='email-invalid')

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('User with the email exists',code='user exists')
        return email
    
    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get('phone_number')
    #     if len(phone_number)==0:
    #         raise forms.ValidationError(
    #             self.error_messages['phone_required'],
    #             code='phone_required'
    #         )
        
    #     if len(phone_number)<5:
    #         raise forms.ValidationError('Phone number must be in format +[number]-[more than 6 numbers less than 15 numbers ]')
    #     if CustomUser.objects.filter(phone_number=phone_number).exists():
    #         raise forms.ValidationError('A user with similiar phone number exists')
    #     return phone_number
    

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password)<5:
            raise forms.ValidationError(
                self.error_messages['password_required'],
                code='password_to_short'
            )
        return password

    def save(self, commit=True):
        user = super(SRegForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
          user.save()
        return user
   
    

class PRegForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        'username_required': ("User name is a required field."),
          'phone_required':("Phone number is required"),
        'password_required':("Pasword must contain atleast 5 characters"),
        'email_required':("email is required")
    }
    password1 = forms.CharField(label=("Password"),
                              widget=forms.PasswordInput)
 

    class Meta:
     model = Professor
     fields = [ 'email','username','password']

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password and password1 and password != password1:
          raise forms.ValidationError(
            self.error_messages['password_mismatch'],
            code='password_mismatch',
        )
        return password1

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username)==0:
            raise forms.ValidationError(
                self.error_messages['username_required'],
                code='username_required'
            )
        return username
    
    def clean_email(self):
        email= self.cleaned_data.get('email')
        if  len(email)==0:
            raise forms.ValidationError(
                self.error_messages['email_required'],
                code='email_required'
            )
        if '@' not in email:
            raise forms.ValidationError('That is not a valid email address ',code='email-invalid')

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('User with the email exists',code='user exists')
        return email
    
    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get('phone_number')
    #     if len(phone_number)==0:
    #         raise forms.ValidationError(
    #             self.error_messages['phone_required'],
    #             code='phone_required'
    #         )
    #     if len(phone_number)<5:
    #         raise forms.ValidationError('Phone number must be in format +[number]-[more than 6 numbers less than 15 numbers ]')
    #     if CustomUser.objects.filter(phone_number=phone_number).exists():
    #         raise forms.ValidationError('A user with similiar phone number exists')
    #     return phone_number
        
        
    

    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if len(password)<5:
            
            raise forms.ValidationError(
                self.error_messages['password_required'],
                code='password_to_short'
            )
        return password

    def save(self, commit=True):
        user = super(PRegForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
          user.save()
        return user
   
    
   

class SignForm(forms.Form):
   
    email = forms.EmailField(
        label=("email"),
    
        widget=forms.EmailInput(),
    )

    password = forms.CharField(
        label=("Password"),

        widget=forms.PasswordInput(),
    )

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(email)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }
    
    def clean_email(self):
        email= self.cleaned_data.get('email')
        if  len(email)==0:
            raise forms.ValidationError(
                self.error_messages['email_required'],
                code='email_required'
            )
        if '@' not in email:
            raise forms.ValidationError('That is not a valid email address ',code='email-invalid')

        
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if len(password)==0:
           
            raise forms.ValidationError(
            'Password field is empty ',
                code='password_to_short'
            )
        return password

    # def __init__(self, request=None, *args, **kwargs):
    #     """
    #     The 'request' parameter is set for custom auth use by subclasses.
    #     The form data comes in via the standard 'data' kwarg.
    #     """
    #     # self.request = request
    #     # self.user_cache = None
    #     # self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
    #     super().__init__(*args, **kwargs)
    


    # def clean(self):
    #     email = self.cleaned_data.get("email")
    #     password = self.cleaned_data.get("password")

    #     if email is not None and password:
    #         self.user_cache = authenticate(
    #             self.request, username=email, password=password
    #         )
    #         if self.user_cache is None:
    #             raise self.get_invalid_login_error()
    #         else:
    #             self.confirm_login_allowed(self.user_cache)

    #     return self.cleaned_data
    
    # def confirm_login_allowed(self, user):
       
    #     if not user.is_active:
    #         raise ValidationError(
    #             self.error_messages["inactive"],
    #             code="inactive",
    #         )
    
    # def get_user(self):
    #     return self.user_cache
    
    # def get_invalid_login_error(self):
    #     return ValidationError(
    #         self.error_messages["invalid_login"],
    #         code="invalid_login",
    #         params={"email": self.username_field.verbose_name},
    #     )



# class UserRegistrationForm(forms.ModelForm):
#   error_messages = {
#     'password_mismatch': ("The two password fields didn't match."),
#     'username_required': ("User name is a required field.")
#   }
#   password1 = forms.CharField(label=("Password"),
#                               widget=forms.PasswordInput)
 

#   class Meta:
#     model = CustomUser
#     fields = [ 'email', 'Phone_number','username','password']

#   def clean_password1(self):
#     password = self.cleaned_data.get("password")
#     password1 = self.cleaned_data.get("password1")
#     if password and password1 and password != password1:
#       raise forms.ValidationError(
#         self.error_messages['password_mismatch'],
#         code='password_mismatch',
#       )
#     return password1

#   def clean_user_name(self):
#     username = self.cleaned_data.get('username')
#     if not username:
#       raise forms.ValidationError(
#         self.error_messages['username required'],
#         code='username_required'
#       )
#     return username

#   def save(self, commit=True):
#     user = super(UserRegistrationForm, self).save(commit=False)
#     user.set_password(self.cleaned_data["password"])
#     if commit:
#       user.save()
#     return user