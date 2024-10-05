from telnetlib import SSPI_LOGON

from django.db import models

from apps.shared.models import SlugStampedModel, TimeStampedModel


class Profession(SlugStampedModel):
    name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Technology(SlugStampedModel):
    name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

