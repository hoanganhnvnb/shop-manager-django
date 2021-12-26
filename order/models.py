from django.db import models

from user.models import CustomerUser
from cart.models import Cart
from notification.models import Notification
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)
    order_total = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            pass
        else:
            if self.is_completed:
                for user in CustomerUser.objects.all().filter(is_superuser=True):
                    title_noti = "Thu ngân đã thanh toán hóa đơn " + str(self.pk)
                    content_noti = "Thu ngân đã thanh toán thành công hóa đơn " + str(self.pk) + " cho user " + self.user.username
                    noti = Notification(title=title_noti, content=content_noti, user=user)
                    noti.save()
                    
                t_cus = "Bạn đã thanh toán thành công"
                c_cus = "Bạn đã thanh toán thành công hóa đơn: " + str(self.pk) + " trị giá: " + str(self.order_total)
                noti_cus = Notification(title=t_cus, content=c_cus, user=self.user)
                noti_cus.save() 
                    
        # This code only happens if the objects is
        # not in the database yet. Otherwise it would
        # have pk
        super(Order, self).save(*args, **kwargs)