from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import BookingSerializer, StudentBookingSerializer
from .models import Booking
from accounts.permissions import IsStudent, IsCustodianOrAdmin

# Create your views here.


class BookingListCreateView(generics.ListCreateAPIView):
    # serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            return Booking.objects.filter(student_id=user)
        return Booking.objects.all()

    def get_serializer_class(self):
        user = self.request.user
        if user.role == 'student':
            return StudentBookingSerializer
        return BookingSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsStudent()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(student_id=self.request.user)


class BookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    # serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsCustodianOrAdmin()]
        return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        user = self.request.user
        if user.role == 'student':
            return StudentBookingSerializer
        return BookingSerializer
