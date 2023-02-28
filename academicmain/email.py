from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import threading

def sendEmail(request,res,template_n,context):
    
    html_content = render_to_string(template_n, context)
    text_content = strip_tags(html_content)
    thread = threading.Thread(target=emailSender, args=("Welcome to BenBrands", text_content,html_content,res))
    thread.start()
    return HttpResponse("Email Sent successfully")


def emailSender(subject, text_content,html_content, reciepants):
    email = EmailMultiAlternatives(
        subject,
        text_content,
        settings.EMAIL_HOST_USER ,
        reciepants
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()
