from rest_framework import generics, permissions, filters
from .models import Event
from.serializers import EventSerializer
from django.utils import timezone

# Event creation
class CreateEventView(generics.CreateAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Event listing
class EventListApiView(generics.ListAPIView):
    queryset=Event.objects.all().order_by("-created_at")
    serializer_class=EventSerializer
    permission_classes=[permissions.IsAuthenticated]

# View upcoming events
class UpcomingEventView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(event_date__gt=timezone.now()).order_by("event_date")
    
# View a single event
class EventDetailView(generics.RetrieveAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    permission_classes=[permissions.AllowAny]

# Update an event
class UpdateEventView(generics.UpdateAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_update(self, serializer):
        event=self.get_object()
        if event.created_by !=self.request.user:
            raise PermissionError("You are not allowed to edit this event!")
        serializer.save()

# Delete an event
class DeleteEventView(generics.DestroyAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.created_by != self.request.user:
            raise PermissionError("You can not delete this event!")
        instance.delete()

# Search for an event using keywords
class EventSearchView(generics.ListAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    permission_classes=[permissions.AllowAny]
    filter_backends=[filters.SearchFilter, filters.OrderingFilter]
    search_fields=["title", "description"]
    ordering_fields=["event_date", "created_at"]
    ordering=["event_date"]