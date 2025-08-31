from django.db import models
from django.conf import settings

class Event(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    location=models.CharField(max_length=255)
    event_date=models.DateTimeField()
    capacity=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="organized_events")

    def __str__(self):
        return self.title