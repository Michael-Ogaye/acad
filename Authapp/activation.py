from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator as token_gen
from academicmain.email import sendEmail
def activate_account(request,user):
     cntx_em={  
                'user': user,  
                'domain': get_current_site(request).domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':token_gen.make_token(user),
                'protocol':'http'
            }
     
     sendEmail(request,[user.email],'Authapp/activation.html',cntx_em)
