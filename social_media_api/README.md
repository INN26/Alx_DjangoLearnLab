# Social Media API

This is a Django-based social media API with user authentication.

## Setup Instructions

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`

## Endpoints

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `GET /api/auth/profile/`