from telnetlib import SSPI_LOGON

from django.db import models

from apps.shared.models import SlugStampedModel


# Create your models here.
class Profession(SlugStampedModel):
    name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)


class Technology(SlugStampedModel):
    name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
