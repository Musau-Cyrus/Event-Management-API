from rest_framework import generics, permissions, status
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.response import Response

# Book an event
class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes=[permissions.IsAuthenticated]

# Cancel Booking
class BookingCancelView(generics.DestroyAPIView):
    queryset=Booking.objects.all()
    permission_classes=[permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        booking_id=kwargs.get("pk")
        try:
            booking = Booking.objects.get(id=booking_id, user=request.user)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found!"})
        
        # Increase event capacity back since user has canceled their booking
        event = booking.event
        event.capacity += 1
        event.save()

        booking.delete()
        return Response({"message": "Booking cancelled successfully!"}, status=status.HTTP_200_OK)