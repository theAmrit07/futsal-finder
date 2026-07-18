# Futsal Finder API

A REST API backend for finding futsal matches and teammates in your city.

## The Problem

Finding people to play futsal with is harder than it should be. Even when you find an available futsal court, getting enough players to form two teams is a challenge — not everyone has the same free time. Futsal Finder solves this by letting players post open matches and others join them.

## Features

- Register and login with JWT authentication
- Create a futsal match with location, date, time and available slots
- Browse all open matches
- Join a match (automatically closes when slots are full)
- Leave a match (reopens slot for others)
- Match status updates automatically (open → full)

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Deployment:** (coming soon)

## API Endpoints

```
POST   /api/auth/register/          Create a new account
POST   /api/auth/login/             Login and get JWT token
GET    /api/matches/                List all open matches
POST   /api/matches/                Create a new match
GET    /api/matches/:id/            Get match details
PUT    /api/matches/:id/            Update your match
DELETE /api/matches/:id/            Delete your match
POST   /api/matches/:id/join/       Join a match
POST   /api/matches/:id/leave/      Leave a match
```

## Running Locally

### Prerequisites
- Python 3.11+
- PostgreSQL

### Setup

```bash
# Clone the repo
git clone https://github.com/theAmrit07/futsal-finder.git
cd futsal-finder

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Fill in your values

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

## Environment Variables

Create a `.env` file in the root directory:

```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=futsalfinder
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Author

**Amrit Chataut**
[GitHub](https://github.com/theAmrit07) · [LinkedIn](https://linkedin.com/in/amrit-chataut-426949246)