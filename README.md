# 🧠 Django Backend Assignment – Internship Submission

This project demonstrates backend skills using Django REST Framework (DRF), Token-based Authentication, Celery for background tasks, Redis as a broker, and a Telegram Bot integration.

---

## 📂 Project Features

✅ Django REST Framework (DRF)  
✅ JWT / Token Authentication  
✅ Celery with Redis for async tasks  
✅ Welcome email sent after registration  
✅ Telegram bot integration (/start command stores user)  
✅ Clean, production-ready code  
✅ `.env` based secrets and configuration

---

## ⚙️ Environment Variables

Create a `.env` file in the project root with:

```env
SECRET_KEY=your_django_secret_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
REDIS_URI=your_redis_connection_url
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ritesh2004/Django-Assignment.git
cd assignment
```

## Without Docker

### 2. Create a Virtual Environment (UV)

```bash
pip install uv
uv venv
.venv/Scripts/activate 
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Django Server

```bash
python manage.py runserver
```

---

## 🧵 Celery & Redis Setup

### Start Redis Server

```bash
# via Docker
docker run -d -p 6379:6379 redis --requirepass yourpassword
```

### Run Celery Worker

```bash
celery -A assignment worker --loglevel=info --pool=solo
```

---

## 🤖 Telegram Bot

### Run the Telegram Bot

```bash
python telegram_bot/bot.py
```

* Sends a welcome message when user types `/start`
* Stores Telegram username in DB

---

## 🔐 API Overview

| Method | Endpoint                | Auth Required  | Description                                        |
| ------ | ----------------------- | -------------  | -------------------------------------------------- |
| GET    | `/api/v1/users/`        | ✅ Yes         | Protected Endpoint to Get all Telegram Users       |
| GET    | `/api/v1/users/<id>/`   | ✅ Yes         | Protected Endpoint to Get a specific Telegram User |
| POST   | `/api/v1/users/`        | ✅ Yes         | Protected Endpoint to Create a Telegram User       |
| PUT    | `/api/v1/users/<id>/`   | ✅ Yes         | Protected Endpoint to Update a Telegram User       |
| POST   | `/api/v1/register/`     | ❌ No          | Register a new user                                |
| POST   | `/api/v1/login/`        | ❌ No          | Login and Get JWT tokens                           |
| POST   | `/api/v1/token/refresh/`| ❌ No          | Get new access token from refresh token            |

> View `api.http` to get detailed api structure
---

## 🧪 Run All Services with Docker

### Docker Compose (Django + Redis + Celery + Telegram)

```bash
docker-compose up --build
```

> Edit `docker-compose.yml` to include all services and environment variables.

---

## 🛠 Tech Stack

* Django 4.x
* Django REST Framework
* Celery
* Redis
* SQLite
* pytelegrambotapi
* Docker (optional)

---

## 🤝 Contact

* LinkedIn: [Ritesh Pramanik](https://www.linkedin.com/in/ritesh-pramanik-8ba316260)
* Email: [ritesh.work.2004@gmail.com](mailto:ritesh.work.2004@gmail.com)

---
