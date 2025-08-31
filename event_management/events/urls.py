from django.urls import path
from .views import CreateEventView, EventListApiView, UpcomingEventView, EventDetailView, UpdateEventView, DeleteEventView, EventSearchView

urlpatterns = [
    path("create/", CreateEventView.as_view(), name="create-event"),
    path("all/", EventListApiView.as_view(), name="event-list"),
    path("upcoming/", UpcomingEventView.as_view(), name="upcoming-events"),
    path("<int:pk>/", EventDetailView.as_view(), name="event-details"),
    path("<int:pk>/update/", UpdateEventView.as_view(), name="update-event"),
    path("<int:pk>/delete/", DeleteEventView.as_view(), name="delete-event"),
    path("search/", EventSearchView.as_view(), name="search-event"),
]