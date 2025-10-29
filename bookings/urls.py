from django.urls import path
from .views import BookingListCreateView, BookingRetrieveUpdateDestroyView

urlpatterns = [
    path('bookings/', BookingListCreateView.as_view(),
         name='bookings-list-create'),
    path('bookings/<uuid:pk>/',
         BookingRetrieveUpdateDestroyView.as_view(), name='booking-detail'),
]
