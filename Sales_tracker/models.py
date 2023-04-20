from django.db import models

# Define custom user model
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)

# Set custom user model in settings.py

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField()

class StaffMember(models.Model):
    ROLE_CHOICES = (
        ('WAITER', 'Waiter'),
        ('CHEF', 'Chef'),
        ('MANAGER', 'Manager'),
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class Sale(models.Model):
    sale_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    staff_member = models.ForeignKey(StaffMember, on_delete=models.PROTECT)

