# Events App Documentation
The Events App handles event creation, updating, deletion, and viewing.
Every event is linked to the user who created it.

### Base URL:
```swift
/api/events/
```
## Endpoints
## 1. Create Event
```swift
POST /api/events/
```
Authenticated users can create new events.

### Request (Headers):
```makefile
Authorization: Bearer <access_token>
```
### Request Body:
```json
{
  "title": "Tech Conference 2025",
  "description": "Annual tech conference on AI and Cloud",
  "location": "Nairobi, Kenya",
  "date": "2025-12-15T09:00:00Z",
  "capacity": 100
}
```
### Response:
```json
{
  "id": "64fcbbe5a2d9a5d89b7b2a12",
  "title": "Tech Conference 2025",
  "description": "Annual tech conference on AI and Cloud",
  "location": "Nairobi, Kenya",
  "date": "2025-12-15T09:00:00Z",
  "capacity": 100,
  "available_seats": 100,
  "created_by": "john_doe",
  "created_at": "2025-08-30T12:00:00Z"
}
```
## 2. View All Events
```swift
GET /api/events/
```
Fetches all available events.

### Response:
```json
[
  {
    "id": "64fcbbe5a2d9a5d89b7b2a12",
    "title": "Tech Conference 2025",
    "location": "Nairobi, Kenya",
    "date": "2025-12-15T09:00:00Z",
    "capacity": 100,
    "available_seats": 100,
    "created_by": "john_doe"
  },
  {
    "id": "64fcbbe5a2d9a5d89b7b2a15",
    "title": "Music Festival",
    "location": "Kisumu, Kenya",
    "date": "2025-09-25T18:00:00Z",
    "capacity": 500,
    "available_seats": 498,
    "created_by": "mary_anne"
  }
]
```
## 3. View Single Event Details
```swift
GET /api/events/<event_id>/
```
Fetch details of a specific event by its ID.

### Response:
```json
{
  "id": "64fcbbe5a2d9a5d89b7b2a12",
  "title": "Tech Conference 2025",
  "description": "Annual tech conference on AI and Cloud",
  "location": "Nairobi, Kenya",
  "date": "2025-12-15T09:00:00Z",
  "capacity": 100,
  "available_seats": 100,
  "created_by": "john_doe",
  "created_at": "2025-08-30T12:00:00Z"
}
```
## 4. Update Event
```swift
PUT/PATCH /api/events/<event_id>/
```
Only the event organizer (creator) can update their event.

### Request Body:
```json
{
  "title": "Tech Conference 2025 - Updated",
  "capacity": 120
}
```
### Response:
```json
{
  "id": "64fcbbe5a2d9a5d89b7b2a12",
  "title": "Tech Conference 2025 - Updated",
  "capacity": 120,
  "available_seats": 120,
  "created_by": "john_doe"
}
```
## 5. Delete Event
```swift
DELETE /api/events/<event_id>/
```
Only the event organizer can delete their event.

### Response:
```json
{
  "message": "Event deleted successfully."
}
```
## 6. View Upcoming Events
```swift
GET /api/events/upcoming/
```
Lists events with a future date.

### Response:
```json
[
  {
    "id": "64fcbbe5a2d9a5d89b7b2a12",
    "title": "Tech Conference 2025",
    "date": "2025-12-15T09:00:00Z"
  }
]
```
## 7. Search / Filter Events
```swift
GET /api/events/search/?q=tech
```
Filters events by keyword (in title or description).

### Response:
```json
[
  {
    "id": "64fcbbe5a2d9a5d89b7b2a12",
    "title": "Tech Conference 2025",
    "location": "Nairobi, Kenya",
    "date": "2025-12-15T09:00:00Z",
    "created_by": "john_doe"
  }
]
```