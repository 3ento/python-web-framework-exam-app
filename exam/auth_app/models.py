from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from exam.auth_app.managers import AppUserManager

# Create your models here.
# UserModel = get_user_model()

class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=25,
        unique=True,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )

    # User credentials consist of `username` and `password`
    USERNAME_FIELD = 'username'

    objects = AppUserManager()

class Profile(models.Model):

    MALE = 'he/him'
    FEMALE = 'she/her'
    NB = 'they/them'

    PRONOUNS = [(x, x) for x in (MALE, FEMALE, NB)]

    first_name = models.CharField(
        max_length=25,
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    pronouns = models.CharField(
        max_length=max(len(x) for x, _ in PRONOUNS),
        choices=PRONOUNS,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        default="https://t4.ftcdn.net/jpg/02/15/84/43/360_F_215844325_ttX9YiIIyeaR7Ne6EaLLjMAmy4GvPC69.jpg",
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )