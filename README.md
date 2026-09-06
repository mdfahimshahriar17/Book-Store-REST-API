# Book Store REST API

A Django REST Framework (DRF) based REST API for managing books with authentication, filtering, searching, ordering, pagination, throttling, and Postman testing.

## Features

- User registration with token generation
- Token-based authentication
- Book CRUD operations
- Public read access for books
- Authenticated users can create, update, and delete books
- Filter books by author
- Search books by title
- Order books by price (ascending/descending)
- Pagination with 5 books per page
- Anonymous throttling: 20 requests/minute
- Authenticated throttling: 50 requests/minute
- Postman collection for API testing

## Technologies

- Python
- Django
- Django REST Framework
- django-filter
- SQLite (development database)
- Postman

## Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Book-Store-REST-API
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` has not been created yet:

```bash
pip install django djangorestframework django-filter
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

API base URL:

```text
http://127.0.0.1:8000/
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/account/register/` | Register a new user |
| POST | `/account/login/` | Login and obtain a token |
| POST | `/account/logout/` | Logout and delete the user's token |

### Book CRUD

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/books/` | Get all books |
| POST | `/api/books/` | Create a new book |
| GET | `/api/books/<id>/` | Get a specific book |
| PUT | `/api/books/<id>/` | Update a book |
| PATCH | `/api/books/<id>/` | Partially update a book |
| DELETE | `/api/books/<id>/` | Delete a book |

## Filtering, Searching & Ordering

### Filter by author

```text
/api/books/?author=<author>
```

### Search by title

```text
/api/books/?search=<title>
```

### Order by price

Ascending:

```text
/api/books/?ordering=price
```

Descending:

```text
/api/books/?ordering=-price
```

## Pagination

Books are returned 5 per page.

```text
/api/books/
```

Second page:

```text
/api/books/?page=2
```

## Authentication

For protected Book API operations, send the token in the request header:

```text
Authorization: Token <your-token>
```

The token is returned after successful registration or login.

## Throttling

- Anonymous users: 20 requests per minute
- Authenticated users: 50 requests per minute

## Postman Collection

The Postman collection contains:

- Register API
- Login API
- Book - GET All
- Book - GET Detail
- Book - POST (Create)
- Book - PUT (Update)
- Book - PATCH
- Book - DELETE

## Author

**MD. Fahim Shahriar**