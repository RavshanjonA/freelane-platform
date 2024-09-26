from django.db import models


class AccountRole(models.TextChoices):
    EMPLOYEE = 'employee', "Employee"
    CUSTOMER = 'customer', "Customer"
