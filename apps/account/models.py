from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.account.choices import AccountRole
from apps.shared.models import TimeStampedModel


class Account(AbstractUser, TimeStampedModel):
    phone = PhoneNumberField(unique=True, region="UZ")
    is_active = models.BooleanField(default=False)
    role = models.CharField(max_length=255, choices=AccountRole.choices)


class AccountInfo(TimeStampedModel):
    bio = models.TextField(null=True)
    profession = models.ForeignKey(to="technology.Profession", on_delete=models.SET_NULL, null=True)
    technologies = models.ManyToManyField("technology.Technology")
    is_visible = models.BooleanField(default=False)
