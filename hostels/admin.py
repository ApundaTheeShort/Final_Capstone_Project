from django.contrib import admin
from .models import Hostel, Rooms

class HostelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'capacity', 'custodian_id')
    search_fields = ('name', 'location')

class RoomsAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_number', 'room_type', 'price_per_semester', 'hostel', 'is_available')
    list_filter = ('is_available', 'room_type', 'hostel')

admin.site.register(Hostel, HostelAdmin)
admin.site.register(Rooms, RoomsAdmin)
