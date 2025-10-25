from rest_framework import serializers
from .models import Hostel, Rooms


class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ['id', 'name', 'location', 'capacity',
                  'description', 'custodian_id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_capacity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Capacity must be a positive integer.")
        return value

    def validate_custodian_id(self, value):
        if value.role != 'custodian':
            raise serializers.ValidationError(
                "The assigned user must have the role of 'custodian'.")
        return value


class StudentHostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ['name', 'location', 'capacity', 'description']


class CustodianHostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ['id', 'name', 'location', 'capacity',
                  'description', 'custodian_id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class RoomSerializer(serializers.ModelSerializer):
    hostel_name = serializers.ReadOnlyField(source='hostel.name')

    class Meta:
        model = Rooms
        fields = ['hostel_name', 'room_id', 'room_number', 'room_type',
                  'price_per_semester', 'hostel', 'is_available', 'created_at', 'updated_at']
        read_only_fields = ['room_id', 'created_at', 'updated_at']

    def validate_price_per_semester(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price per semester must be a positive value.")
        return value

    def validate_room_number(self, value):
        if not value:
            raise serializers.ValidationError(
                "Room number cannot be empty.")
        return value


class StudentRoomSerializer(serializers.ModelSerializer):
    hostel_name = serializers.ReadOnlyField(source='hostel.name')

    class Meta:
        model = Rooms
        fields = ['hostel_name', 'room_number', 'room_type',
                  'price_per_semester', 'is_available']
