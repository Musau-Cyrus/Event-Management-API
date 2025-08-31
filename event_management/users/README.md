# Users App – API Documentation
The Users app handles:
- User registration
- Authentication (login with JWT)
- Token refresh & logout
- Fetching user profile

### Base URL:
```swift
http://127.0.0.1:8000/api/users/
```
## 1. Register a New User
### Endpoint:
```swift
POST /api/users/register/
```
### Request Body:
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "StrongPassword123!"
}
```

### Response:
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com"
}
```
## 2. Login (Obtain JWT Tokens)
### Endpoint:
```swift
POST /api/users/login/
```
### Request Body:
```json
{
  "email": "john@example.com",
  "password": "StrongPassword123!"
}
````

### Response:
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR..."
}
````

`Note:`The access token is used in API requests.
Add it in headers:
```makefile
Authorization: Bearer <access_token>
```
## 3. Refresh Token
### Endpoint:
```swift
POST /api/users/token/refresh/
```
### Request Body:
```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR..."
}
```

### Response:
```json
{
  "access": "new_access_token_here"
}
```
## 4. Logout (Blacklist Refresh Token)
### Endpoint:
```swift
POST /api/users/logout/
```

### Request Body:
```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR..."
}
```

### Response:
```json
{
  "message": "User logged out successfully"
}
```
## 5. Get User Profile

### Endpoint:
```swift
GET /api/users/me/
```
### Headers:
```makefile
Authorization: Bearer <access_token>
```

### Response
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "date_joined": "2025-08-26T12:30:00Z"
}
```