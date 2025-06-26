from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

# Celery task to send an email asynchronously
# This task can be used to send emails without blocking the main thread,
# allowing for better performance in web applications.
@shared_task
def send_email_task(subject, message, recipient_list):
    """
    A Celery task to send an email asynchronously.
    
    :param subject: Subject of the email
    :param message: Body of the email
    :param from_email: Sender's email address
    :param recipient_list: List of recipient email addresses
    """
    from_email = settings.EMAIL_HOST_USER  # Use the email host user from settings
    send_mail(subject, message, from_email , recipient_list, fail_silently=False)