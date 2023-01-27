from django.contrib import admin
from .models import Product
class ProcuctAdmin(admin.ModelAdmin):
    list_display = ('name','content', 'price')
# Register your models here.
admin.site.register(Product, ProcuctAdmin)
# Register your models here.
# Register your models here.
