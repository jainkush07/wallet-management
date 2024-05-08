from django.contrib.auth.models import AbstractUser, User, Group, Permission
from django.db import models
from django.utils.translation import gettext as _ 

class CustomUser(AbstractUser):
    # Add your custom fields here
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'  # Set email as the unique identifier for authentication
    REQUIRED_FIELDS = []  # Remove any other required fields, as email is sufficient

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # Specify custom related names for groups and user permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user'
    )
    
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Expense(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('ExpenseCategory', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)