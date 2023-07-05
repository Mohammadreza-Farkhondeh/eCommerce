from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,)
from django.utils.crypto import get_random_string
from django.db.models import EmailField, BooleanField


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

        # User only provide email and this method create an account with that email and a random password
        # The password will send to user email, then user can log in with the email and password
        email = self.normalize_email(email).lower()
        password = get_random_string(length=12)

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


class UserAccount(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a personalized user model

    Email is required. Other fields are optional.
    """
    email = EmailField(unique=True, db_index=True, max_length=255)

    # Now user will get a random password and account is activa at first
    # We could set account is_active False at first then active it with a code or link sent to user email
    # Then user can set desired password, of course now user can change password.
    # TODO: implement email verification not email password-postman
    is_active = BooleanField(default=True, verbose_name="active status")
    is_staff = BooleanField(default=False, verbose_name='staff status')

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
