from django.contrib import admin
from .models import Coupon



class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','use_from','use_to']


admin.site.register(Coupon,CouponAdmin)
