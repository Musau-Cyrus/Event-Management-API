from rest_framework import generics, permissions
from .models import Event
from.serializers import EventSerializer
from django.utils import timezone

class CreateEventView(generics.CreateAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class EventListApiView(generics.ListAPIView):
    queryset=Event.objects.all().order_by("-created_at")
    serializer_class=EventSerializer
    permission_classes=[permissions.IsAuthenticated]

class UpcomingEventView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(event_date__gt=timezone.now()).order_by("event_date")