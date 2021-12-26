from django.db import models

from category.models import Category
# Create your models here.
import FCMManager as fcm
from notification.models import Notification
from user.models import CustomerUser
from report.models import Report

class Items(models.Model):
    barcode = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    importPrice = models.IntegerField(default=0)
    sellPrice = models.IntegerField(default=0)

    quantity = models.IntegerField(default=0)

    companyName = models.CharField(max_length=50)

    active = models.BooleanField(default=True)
    
    quantity_sold = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            for user in CustomerUser.objects.all().filter(is_superuser=False):
                title_noti = "Cửa hàng đã nhập hàng hóa mới"
                content_noti = self.title + " đã được cửa hàng nhập về."
                noti = Notification(title=title_noti, content=content_noti, user=user)
                noti.save()
                report = Report.objects.get(pk=1)
                report.total_price_import = report.total_price_import + self.importPrice * self.quantity
                report.save()
        else:
            if self.quantity <= 10:
                    for user in CustomerUser.objects.all().filter(is_superuser=True):
                        title_noti = self.title + " trong kho đã sắp hết!"
                        content_noti = self.title + " đã sắp hết, mau chóng nhập thêm hàng hóa nếu cần."
                        noti = Notification(title=title_noti, content=content_noti, user=user)
                        noti.save()
            
            if self.quantity == 10:
                    for user in CustomerUser.objects.all().filter(is_superuser=True):
                        title_noti = self.title + " trong kho đã hết!"
                        content_noti = self.title + " đã hết, hãy nhập thêm hàng hóa này."
                        noti = Notification(title=title_noti, content=content_noti, user=user)
                        noti.save()
                    
        # This code only happens if the objects is
        # not in the database yet. Otherwise it would
        # have pk
        
        super(Items, self).save(*args, **kwargs)

# class ItemsCategory(models.Model):
#     items = models.ForeignKey(Items)
#     category = models.ForeignKey(Category)


