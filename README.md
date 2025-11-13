# Crego-Internship-Assignment

A simple Django REST API for managing transactions, featuring:
- CRUD operations using Django REST Framework (DRF)
- Redis-powered middleware for tracking total API requests
- PostgreSQL as the database
- Unit tests for models and views

## 🚀 Setup Instructions

### 1️⃣ Clone and Install
```bash
git clone <your_repo_url>
cd fintech_project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2️⃣ Configure Environment
Create a `.env` file in the root directory (already included here):
```env
DB_NAME=fintech_db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
REDIS_HOST=localhost
REDIS_PORT=6379
```

### 3️⃣ Apply Migrations & Run Server
```bash
python manage.py migrate
python manage.py runserver
```

### 4️⃣ Start Redis
```bash
redis-server
```

### 5️⃣ Run Tests
```bash
python manage.py test
```

## 🧠 Middleware Explanation
Every incoming request increments a Redis key `api_request_count`.  
It logs the running total in the console and is accessible via `/api/stats/`.

## 🧩 API Endpoints
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | /api/transactions/ | Create new transaction |
| GET | /api/transactions/ | List all transactions |
| GET | /api/transactions/<id>/ | Retrieve by ID |
| PUT | /api/transactions/<id>/ | Update transaction |
| DELETE | /api/transactions/<id>/ | Delete transaction |
| GET | /api/stats/ | Get total requests and total transactions |
