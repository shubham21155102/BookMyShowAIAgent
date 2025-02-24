from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerTable(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    preferences = models.JSONField(blank=True, null=True)

    # Fixing reverse accessor clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customer_users",  # Unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customer_users_permissions",  # Unique related_name
        blank=True
    )

    def __str__(self):
        return self.username