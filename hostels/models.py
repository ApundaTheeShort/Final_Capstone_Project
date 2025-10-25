import uuid
from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import CustomUser

# Create your models here.


class Hostel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,
                          unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    custodian_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                     related_name='hostels', limit_choices_to={'role': 'custodian'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.custodian_id.role != 'custodian':
            raise ValidationError(
                "The assigned user must have the role of 'custodian'.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Rooms(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]

    room_id = models.UUIDField(primary_key=True, editable=False,
                               unique=True, default=uuid.uuid4)
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(
        max_length=10, choices=ROOM_TYPES, default='single')
    price_per_semester = models.DecimalField(max_digits=10, decimal_places=2)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE,
                               related_name='rooms')
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('hostel', 'room_number')

    def __str__(self):
        return f"{self.hostel.name} - Room {self.room_number}"
