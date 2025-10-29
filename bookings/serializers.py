from rest_framework import serializers
from .models import Booking
from hostels.models import Rooms


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['student_id']


class StudentBookingSerializer(serializers.ModelSerializer):
    hostel_name = serializers.ReadOnlyField(source='room_id.hostel.name')
    room_number = serializers.ReadOnlyField(source='room_id.room_number')
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Rooms.objects.all(), write_only=True)
    price = serializers.ReadOnlyField(source='room_id.price_per_semester')
    room_type = serializers.ReadOnlyField(source='room_id.room_type')

    class Meta:
        model = Booking
        # fields = '__all__'
        fields = ['hostel_name', 'room_number', 'room_type', 'id', 'student_id',
                  'check_in_date', 'check_out_date', 'status', 'room_id', 'price']
        read_only_fields = ['status', 'student_id']

    def validate(self, data):
        if data['check_in_date'] >= data['check_out_date']:
            raise serializers.ValidationError(
                "Check-out date must be after check-in date.")
        elif Booking.objects.filter(room_id=data['room_id'], status='approved').exists():
            raise serializers.ValidationError(
                "The room has already been booked")
        return data
