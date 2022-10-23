from email.headerregistry import Group
from django.contrib import admin
from .models import TRACKING, CONTACT
from django.contrib.auth.models import Group
# Register your models here.
class TRACK(admin.ModelAdmin):
    model = TRACKING
    fieldsets = (
        ('EXPRESS COURIER',{'fields': ('TRACKING_ID','ORIGIN','DESTINATION',)}),
        ('SENDER',{'fields': ('SENDER_NAME','PHONE','EMAIL','BOOKING_DATE',)}),
        ('RECIPIENT',{'fields': ('RECIPIENT_NAME','RECIPIENT_PHONE','RECIPIENT_EMAIL','SHIPPING_DATE',)}),
        ('PACKAGE CONTENT',{'fields': ('COURIER','CONTENTS','QUANTITY','WEIGHT', 'STATUS',)}),
        ('PACKAGE LOCATION',{'fields': ('PACKAGE_LOCATION',)}),
    )

    
admin.site.unregister(Group)
admin.site.register(TRACKING, TRACK)
admin.site.register(CONTACT)