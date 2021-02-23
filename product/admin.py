from django.contrib import admin

# Register your models here.
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ( 'title', 'description', 'image','admin_photo')
    list_display = ['id', 'title', 'short_description', 'admin_photo']
    readonly_fields = ('admin_photo',)
    
