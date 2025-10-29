import uuid
from django.db import models
from accounts.models import CustomUser
from hostels.models import Rooms, Hostel
# Create your models here.


class Booking(models.Model):
    STATUS = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    ]
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    student_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    room_id = models.ForeignKey(
        Rooms, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student_id', 'room_id')
        ordering = ['-created_at']

    def __str__(self):
        return f"Booking {self.id} by {self.student_id.username} for Room {self.room_id.room_number}"
