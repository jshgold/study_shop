from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'id','name','slug'
    ]


admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

admin.site.register(Product,ProductAdmin)
