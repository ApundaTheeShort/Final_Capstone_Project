from django.urls import path
from .views import HostelListCreateAPIView, HostelRetrieveUpdateDestroyAPIView, RoomListCreateAPIView, RoomRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('hostels/', HostelListCreateAPIView.as_view(), name='hostel-list-create'),
    path('hostels/<uuid:pk>/', HostelRetrieveUpdateDestroyAPIView.as_view(),
         name='hostel-retrieve-update-destroy'),
    path('rooms/', RoomListCreateAPIView.as_view(), name='room-list-create'),
    path('rooms/<uuid:pk>/', RoomRetrieveUpdateDestroyAPIView.as_view(),
         name='room-retrieve-update-destroy'),
]

# path('hostels/<int:pk>/',
#      HostelRetrieveUpdateDestroyAPIView.as_view(), name='hostels'),
# ]
