from django.urls import path
from .views import BookingCreateView, BookingCancelView

urlpatterns = {
    path("<int:pk>/book/", BookingCreateView.as_view(), name="event-booking"),
    path('<int:pk>/cancel/', BookingCancelView.as_view(), name='booking-cancel'),
}