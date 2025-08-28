from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username", read_only=True)

    class Meta:
        model = Event
        fields = "__all__"
