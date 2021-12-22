from django.db import models

# Create your models here.
from user.models import CustomerUser


class Notification(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)
