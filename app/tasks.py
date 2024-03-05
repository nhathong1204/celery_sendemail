from celery import shared_task
from .email import send_review_email

@shared_task
def send_email_task(name, email, review):
    return send_review_email(name, email, review)