from django.core.mail import send_mail
from django.conf import settings

def sendMail(email, template, subject):
	if template is not None:
		send_mail("Customer Query", None, email, [settings.EMAIL_HOST_USER], html_message=template)

	else:
		send_mail("Customer Query", "Customer has booked the tour" , email, [settings.EMAIL_HOST_USER])
