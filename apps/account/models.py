from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.account.choices import AccountRole, NotificationType
from apps.account.managers import UserManager
from apps.shared.models import TimeStampedModel


class Account(AbstractUser, TimeStampedModel):
    phone = PhoneNumberField(unique=True, region="UZ")
    is_active = models.BooleanField(default=False)
    role = models.CharField(max_length=255, choices=AccountRole.choices)
    USERNAME_FIELD = 'phone'
    objects = UserManager()

    def __str__(self):
        return str(self.phone)


class AccountInfo(TimeStampedModel):
    bio = models.TextField(null=True)
    profession = models.ForeignKey(to="technology.Profession", on_delete=models.SET_NULL, null=True)
    technologies = models.ManyToManyField("technology.Technology")
    is_visible = models.BooleanField(default=False)
    account = models.OneToOneField("account.Account", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account.phone} - {self.is_visible}"


class Notification(TimeStampedModel):
    message = models.TextField()
    account = models.ForeignKey(to="account.AccountInfo", on_delete=models.CASCADE, related_name="notifications")
    is_read = models.BooleanField(default=False)
    type = models.CharField(choices=NotificationType.choices, max_length=12)
    url = models.CharField(max_length=255)

    def mark_as_read(self):
        self.is_read = True
        self.save()
