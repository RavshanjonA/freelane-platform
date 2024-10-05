from django.db import models


class AccountRole(models.TextChoices):
    EMPLOYEE = 'employee', "Employee"
    CUSTOMER = 'customer', "Customer"


class NotificationType(models.TextChoices):
    JOB_ANNOUNCE = "job_announce", "Job Announce"
    JOB_CONTRACT = "job_contract", "Job Contract"
    CHAT_MESSAGE = "chat_message", "Chat Message"
    OTHER = "other", "Other"
