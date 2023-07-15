from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,)
from django.db.models import EmailField, BooleanField
from .managers import UserAccountManager

# TODO: create profile model with oneToOne relationship with UserAccount for saving user information such as name, address ...
# TODO: use django signals to create profile after UserAccount created


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
