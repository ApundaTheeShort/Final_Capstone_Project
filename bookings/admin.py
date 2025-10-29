from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'room_id', 'status', 'check_in_date', 'check_out_date')
    list_filter = ('status', 'check_in_date')

admin.site.register(Booking, BookingAdmin)
