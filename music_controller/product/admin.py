from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
class ProcuctAdmin(admin.ModelAdmin):
    list_display = ('name','content','category', 'user', 'price')
# Register your models here.
admin.site.register(Product, ProcuctAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
# Register your models here.
