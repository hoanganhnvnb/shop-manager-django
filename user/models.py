from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from notification.models import Notification
class CustomerUser(AbstractUser):
    phone_number = models.CharField(default='', max_length=12)
    address = models.CharField(default='', max_length=255)
    token = models.CharField(default='', max_length=1000)

    def __str__(self):
        return str(self.username)
