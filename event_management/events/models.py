from django.db import models
from django.conf import settings

class Event(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    venue=models.CharField(max_length=255)
    date_time=models.DateTimeField()
    capacity=models.PositiveIntegerField()
    created_at=models.DateTimeField()
    organizer=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="organized_events")

    def __str__(self):
        return self.title