from telnetlib import SSPI_LOGON

from django.db import models
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError

from apps.shared.models import SlugStampedModel, TimeStampedModel


class Profession(SlugStampedModel):
    name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        if Profession.objects.filter(name=self.name).exists():
            raise ValidationError(detail={'name': 'This  profession already created'}, code="name")
        self.slug = slugify(self.name)
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    def __str__(self):
        return self.name


class Technology(SlugStampedModel):
    name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        if Technology.objects.filter(name=self.name).exists():
            raise ValidationError(detail={'name': 'This  technology already created'}, code="name")
        self.slug = slugify(self.name)
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    def __str__(self):
        return self.name
