from django.contrib import admin

from .models import Diller
# Register your models here.
@admin.register(Diller)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number')
