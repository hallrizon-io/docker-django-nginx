from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from .Client import Client


class Profile(AbstractUser):
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    phone = models.CharField(max_length=13, blank=True)
    client = models.ForeignKey(Client, db_index=True, related_name='profile', on_delete=models.SET_NULL,
                               null=True, default=None)
    demo = models.BooleanField(default=False)
    objects = UserManager()

    def __str__(self):
        return f'{self.id}'
