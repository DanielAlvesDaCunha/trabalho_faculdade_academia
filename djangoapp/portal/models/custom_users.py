from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_info = models.OneToOneField(
        'portal.UserInfo',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='custom_user_info',

    )


    email = models.EmailField(unique=True, blank=False)
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name="customuser_set",
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name="customuser_set",
        help_text='Specific permissions for this user.',
    )