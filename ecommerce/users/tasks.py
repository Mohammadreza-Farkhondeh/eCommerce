from ecommerce.celery import app
from django.core.mail import send_mail
from django.conf import settings


@app.task
def send_user_password(email, password):
    """
    task for sending user random generated password to user email
    """
    send_mail(
        subject='your eCommerce website login password',
        message=f'Your email registered in eCommerce website. your login password is {password}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )
    return f'password email sent to user with this email :{email}'

