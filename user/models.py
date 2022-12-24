import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel

from .managers import CustomUserManager


# Create your models here.
class User(AbstractBaseUser, TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={"unique": _("A user with that email address already exists.")},
    )
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    profile_image = models.CharField(max_length=250, null=True)
    role = models.CharField(max_length=80)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
