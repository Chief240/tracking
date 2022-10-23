from django.db import models
from django.utils.text import slugify

# Create your models here.
class TRACKING(models.Model):
    TRACKING_ID = models.CharField(max_length=15)
    ORIGIN = models.CharField(max_length=50)
    DESTINATION = models.CharField(max_length=500)
    SENDER_NAME = models.CharField(max_length=50)
    PHONE = models.CharField(max_length=30)
    EMAIL = models.CharField(max_length=50)
    BOOKING_DATE = models.DateField()
    RECIPIENT_NAME = models.CharField(max_length=50)
    RECIPIENT_PHONE = models.CharField(max_length=30)
    RECIPIENT_EMAIL = models.CharField(max_length=50)
    SHIPPING_DATE = models.DateField()
    COURIER = models.CharField(max_length=100)
    CONTENTS = models.CharField(max_length=500)
    QUANTITY = models.CharField(max_length=20)
    WEIGHT = models.CharField(max_length=20)
    STATUS = models.CharField(max_length=50)
    PACKAGE_LOCATION = models.CharField(max_length=50)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.TRACKING_ID)
        super(TRACKING, self).save(*args, **kwargs)

    def __str__(self):
        return self.TRACKING_ID


class CONTACT(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=50000)

    def __str__(self):
        return self.name