from django.contrib import admin
from .models import Room
class RoomAdmin(admin.ModelAdmin):
    list_display = ('code','host','guest_can_pause','votes_to_skip')
# Register your models here.
admin.site.register(Room, RoomAdmin)
# Register your models here.
