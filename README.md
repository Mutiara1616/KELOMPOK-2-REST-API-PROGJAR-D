# Flask REST API Documentation

## User Endpoints

### 1. Get All Users
- **URL:** `/api/users/`
- **Method:** `GET`
- **Success Response:**
  - **Code:** 200
  - **Content:** List of all users
```json
[
    {
        "id": 1,
        "name": "John",
        "email": "john@example.com"
    }
]
```

### 2. Create New User
- **URL:** `/api/users/`
- **Method:** `POST`
- **Data Params:**
```json
{
    "name": "John",
    "email": "john@example.com"
}
```
- **Success Response:**
  - **Code:** 201
  - **Content:** Created user object

### 3. Get User by ID
- **URL:** `/api/users/<id>`
- **Method:** `GET`
- **URL Params:** 
  - `id=[integer]`
- **Success Response:**
  - **Code:** 200
  - **Content:**
```json
{
    "id": 1,
    "name": "John",
    "email": "john@example.com"
}
```
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"message": "User not found"}`

### 4. Update User
- **URL:** `/api/users/<id>`
- **Method:** `PUT`
- **URL Params:**
  - `id=[integer]`
- **Data Params:**
```json
{
    "name": "John Updated",
    "email": "john.updated@example.com"
}
```
- **Success Response:**
  - **Code:** 200
  - **Content:** Updated user object
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"message": "User not found"}`

### 5. Partial Update User
- **URL:** `/api/users/<id>`
- **Method:** `PATCH`
- **URL Params:**
  - `id=[integer]`
- **Data Params:**
```json
{
    "name": "John Patched"
}
```
- **Success Response:**
  - **Code:** 200
  - **Content:** Updated user object
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"message": "User not found"}`
  - **Code:** 400
  - **Content:** `{"message": "Name already exists"}`

### 6. Delete User
- **URL:** `/api/users/<id>`
- **Method:** `DELETE`
- **URL Params:**
  - `id=[integer]`
- **Success Response:**
  - **Code:** 204
  - **Content:** No content
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"message": "User not found"}`

### 7. Search Users
- **URL:** `/api/users/search`
- **Method:** `GET`
- **URL Params:**
  - `name=[string]` (optional)
  - `email=[string]` (optional)
- **Success Response:**
  - **Code:** 200
  - **Content:** List of matching users
```json
[
    {
        "id": 1,
        "name": "John",
        "email": "john@example.com"
    }
]
```
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"message": "No users found matching criteria"}`

### 8. Get All User Emails
- **URL:** `/api/users/emails`
- **Method:** `GET`
- **Success Response:**
  - **Code:** 200
  - **Content:**
```json
{
    "emails": [
        "john@example.com",
        "jane@example.com"
    ]
}
```

### 9. Get User Count
- **URL:** `/api/users/count`
- **Method:** `GET`
- **Success Response:**
  - **Code:** 200
  - **Content:**
```json
{
    "total_users": 10
}
```

### 10. Get Paginated Users
- **URL:** `/api/users/page/<page_number>`
- **Method:** `GET`
- **URL Params:**
  - `page_number=[integer]`
  - `limit=[integer]` (optional, default=5)
- **Success Response:**
  - **Code:** 200
  - **Content:** List of users for specified page
```json
[
    {
        "id": 1,
        "name": "John",
        "email": "john@example.com"
    },
    {
        "id": 2,
        "name": "Jane",
        "email": "jane@example.com"