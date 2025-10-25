from django.shortcuts import render
from rest_framework import generics, permissions
from accounts.permissions import IsAdmin, IsCustodian, IsStudent, IsCustodianOrAdmin
from rest_framework.permissions import IsAuthenticated
from .models import Hostel, Rooms
from .serializers import (HostelSerializer,
                          StudentHostelSerializer,
                          CustodianHostelSerializer,
                          RoomSerializer,
                          StudentRoomSerializer)
# Create your views here.


# class HostelViewSet(viewsets.ModelViewSet):
#     queryset = Hostel.objects.all().order_by('-created_at')
#     serializer_class = HostelSerializer
#     permission_classes = [permissions.IsAuthenticated & IsAdmin]

class HostelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hostel.objects.all().order_by('-created_at')
    serializer_class = HostelSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        user = self.request.user
        if user.is_authenticated and user.role == 'admin':
            return HostelSerializer
        elif user.is_authenticated and user.role == 'custodian':
            return CustodianHostelSerializer
        return StudentHostelSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdmin()]
        return [permissions.IsAuthenticated()]


class HostelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [IsAdmin]


class RoomListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rooms.objects.all().order_by('-created_at')
    serializer_class = RoomSerializer

    def get_serializer_class(self):
        user = self.request.user
        if user.is_authenticated and user.role in ['custodian', 'admin']:
            return RoomSerializer
        return StudentRoomSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsCustodianOrAdmin()]
        return [permissions.IsAuthenticated()]


class RoomRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsCustodianOrAdmin]
