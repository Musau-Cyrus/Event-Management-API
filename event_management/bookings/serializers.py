from rest_framework import serializers
from .models import Booking
from events.models import Event

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=["id", "event", "user", "booked_at"]
        read_only_fields=["id", "user", "booked_at"]

    def create(self, validated_data):
        user=self.context['request'].user
        event=validated_data['event']

        #Check for event capacity
        if event.capacity == 0:
            raise serializers.ValidationError("This event is fully booked")
        
        #Prevent double booking
        if Booking.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("You already booked this event")
        
        # Reduce capacity after a user books
        event.capacity -= 1
        event.save()

        return Booking.objects.create(user=user, event=event)