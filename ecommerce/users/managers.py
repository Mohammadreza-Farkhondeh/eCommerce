from django.contrib.auth.models import BaseUserManager
from django.utils.crypto import get_random_string
from .tasks import send_user_password
from django.core.mail import send_mail
from django.conf import settings
class UserAccountManager(BaseUserManager):
    """
    UserAccountManager for overwriting create_user and create_superuser methods in BaseUserManager
    """
    def _create_user(self, email, **extra_fields):
        """
        Create and save a user with the given email.
        """
        if not email:
            raise ValueError('User must have an email address')

        # User only provides email, and this method creates an account with that email and a random password
        # The password will send to user email, then user can log in with the email and password
        email = self.normalize_email(email).lower()
        password = get_random_string(length=12)

        # email the password to user
        send_user_password.delay(email, password)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, **extra_fields)

    def create_super_user(self, email, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, **extra_fields)
