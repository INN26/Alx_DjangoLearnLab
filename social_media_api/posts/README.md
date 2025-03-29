Register a New User

Endpoint: POST /api/auth/register/

Request:

{
  "username": "testuser",
  "email": "test@example.com",
  "password": "securepassword"
}

Response:

{
  "id": 1,
  "username": "testuser",
  "email": "test@example.com"
}

Login User

Endpoint: POST /api/auth/login/

Request:

{
  "username": "testuser",
  "password": "securepassword"
}

Response:

{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}

Get User Profile (Authenticated)

Endpoint: GET /api/auth/profile/

Headers:

{
  "Authorization": "Bearer <access_token>"
}

Response:

{
  "id": 1,
  "username": "testuser",
  "email": "test@example.com",
  "bio": "Hello!",
  "profile_picture": "url_to_image",
  "followers": []
}

Posts

Create a Post (Authenticated)

Endpoint: POST /api/posts/

Headers:

{
  "Authorization": "Bearer <access_token>"
}

Request:

{
  "title": "My First Post",
  "content": "This is my first post content."
}

Response:

{
  "id": 1,
  "author": "testuser",
  "title": "My First Post",
  "content": "This is my first post content.",
  "created_at": "2025-03-29T08:00:00Z",
  "updated_at": "2025-03-29T08:00:00Z"
}

Retrieve All Posts

Endpoint: GET /api/posts/

Response:

[
  {
    "id": 1,
    "author": "testuser",
    "title": "My First Post",
    "content": "This is my first post content.",
    "created_at": "2025-03-29T08:00:00Z",
    "updated_at": "2025-03-29T08:00:00Z"
  }
]

Retrieve a Specific Post

Endpoint: GET /api/posts/{id}/

Example: GET /api/posts/1/

Response:

{
  "id": 1,
  "author": "testuser",
  "title": "My First Post",
  "content": "This is my first post content.",
  "created_at": "2025-03-29T08:00:00Z",
  "updated_at": "2025-03-29T08:00:00Z"
}

Update a Post (Authenticated, Owner Only)

Endpoint: PUT /api/posts/{id}/

Headers:

{
  "Authorization": "Bearer <access_token>"
}

Request:

{
  "title": "Updated Post Title",
  "content": "Updated content."
}

Response:

{
  "id": 1,
  "author": "testuser",
  "title": "Updated Post Title",
  "content": "Updated content.",
  "created_at": "2025-03-29T08:00:00Z",
  "updated_at": "2025-03-29T08:10:00Z"
}

Delete a Post (Authenticated, Owner Only)

Endpoint: DELETE /api/posts/{id}/

Headers:

{
  "Authorization": "Bearer <access_token>"
}

Response:

{
  "message": "Post deleted successfully."
}

Comments

Create a Comment on a Post (Authenticated)

Endpoint: POST /api/comments/

Headers:

{
  "Authorization": "Bearer <access_token>"
}

Request:

{
  "post": 1,
  "content": "This is a comment."
}

Response:

{
  "id": 1,
  "author": "testuser",
  "post": 1,
  "content": "This is a comment.",
  "created_at": "2025-03-29T08:15:00Z",
  "updated_at": "2025-03-29T08:15:00Z"
}

Retrieve Comments for a Post

Endpoint: GET /api/posts/{id}/comments/

Example: GET /api/posts/1/comments/

Response:

[
  {
    "id": 1,
    "author": "testuser",
    "content": "This is a comment.",
    "created_at": "2025-03-29T08:15:00Z",
    "updated_at": "2025-03-29T08:15:00Z"
  }
]

Update a Comment (Authenticated, Owner Only)

Endpoint: PUT /api/comments/{id}/

Headers:

{
  "Authorization": "Bearer <access_token>"
}

Request:

{
  "content": "Updated comment."
}

Response:

{
  "id": 1,
  "author": "testuser",
  "content": "Updated comment.",
  "created_at": "2025-03-29T08:15:00Z",
  "updated_at": "2025-03-29T08:20:00Z"
}

Delete a Comment (Authenticated, Owner Only)

Endpoint: DELETE /api/comments/{id}/

Headers:

{
  "Authorization": "Bearer <access_token>"
}

Response:

{
  "message": "Comment deleted successfully."
}

Additional Features

Pagination: List endpoints support pagination (e.g., GET /api/posts/?page=2).

Filtering: Posts can be filtered by title or content (e.g., GET /api/posts/?search=keyword).