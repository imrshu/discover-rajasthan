from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task


@shared_task
def sendMail(email, template, subject):
	send_mail(subject, None , email, [settings.EMAIL_HOST_USER], html_message=template)


@shared_task
def clientMail(email, template, subject):
	send_mail(subject, None , settings.EMAIL_HOST_USER, [email] , html_message=template)
