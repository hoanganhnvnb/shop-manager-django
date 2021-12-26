from django.db import models

# Create your models here.
from user.models import CustomerUser
import FCMManager as fcm


class Notification(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            token = []
            if len(self.user.token) > 10:
                token.append(self.user.token)
                fcm.sendPush(title=self.title, msg=self.content, registration_token=token, dataObject={
                    "username": self.user.username,
                })
        # This code only happens if the objects is
        # not in the database yet. Otherwise it would
        # have pk
        super(Notification, self).save(*args, **kwargs)
