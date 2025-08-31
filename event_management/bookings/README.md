# Bookings App Documentation

The Bookings App allows users to register for events, cancel bookings, and view their registered events.
Each booking reduces the event’s available seats until capacity is reached.

## Base URL:
```swift
/api/bookings/
```
## Endpoints
## 1. Register for an Event
```swift
POST /api/bookings/
```
Authenticated users can register for an event.

### Request (Headers):
```makefile
Authorization: Bearer <access_token>
```
### Request Body:
```json
{
  "event": "64fcbbe5a2d9a5d89b7b2a12"
}
```
### Response:
```json
{
  "id": "72ad8c9cbb12490a832fe321",
  "event": {
    "id": "64fcbbe5a2d9a5d89b7b2a12",
    "title": "Tech Conference 2025",
    "date": "2025-12-15T09:00:00Z",
    "location": "Nairobi, Kenya"
  },
  "user": "john_doe",
  "status": "Registered",
  "created_at": "2025-08-31T10:00:00Z"
}
```
## 2. View My Bookings
```swift
GET /api/bookings/
```
Authenticated users can view all events they have registered for.

### Response:
```json
[
  {
    "id": "72ad8c9cbb12490a832fe321",
    "event": {
      "id": "64fcbbe5a2d9a5d89b7b2a12",
      "title": "Tech Conference 2025",
      "date": "2025-12-15T09:00:00Z"
    },
    "status": "Registered",
    "created_at": "2025-08-31T10:00:00Z"
  },
  {
    "id": "72ad8c9cbb12490a832fe322",
    "event": {
      "id": "64fcbbe5a2d9a5d89b7b2a15",
      "title": "Music Festival",
      "date": "2025-09-25T18:00:00Z"
    },
    "status": "Registered",
    "created_at": "2025-08-31T11:30:00Z"
  }
]
```
## 3. Cancel a Booking
```swift
DELETE /api/bookings/<booking_id>/cancel/
```
Authenticated users can cancel their booking.
When cancelled, the event’s available seats increase by 1.

### Response:
```json
{
  "message": "Booking cancelled successfully.",
  "event": {
    "id": "64fcbbe5a2d9a5d89b7b2a12",
    "title": "Tech Conference 2025",
    "available_seats": 101
  }
}
```
## 4. View Bookings for a Specific Event (Organizer Only)
```swift
GET /api/bookings/event/<event_id>/
```
Event organizers can see who registered for their event.

### Response:
```json
[
  {
    "id": "72ad8c9cbb12490a832fe321",
    "user": "john_doe",
    "status": "Registered"
  },
  {
    "id": "72ad8c9cbb12490a832fe322",
    "user": "mary_anne",
    "status": "Registered"
  }
]
```