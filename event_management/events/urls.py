from django.urls import path
from .views import CreateEventView, EventListApiView, UpcomingEventView

urlpatterns = [
    path("create/", CreateEventView.as_view(), name="create-event"),
    path("all/", EventListApiView.as_view(), name="event-list"),
    path("upcoming/", UpcomingEventView.as_view(), name="upcoming-events"),
]