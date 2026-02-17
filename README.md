# Todo API (FastAPI + SQLite + Docker)

A simple CRUD Todo API built with FastAPI, SQLAlchemy, and SQLite.
Dockerized with Dockerfile + docker-compose.

## Features
- Create task
- List tasks
- Get task by id
- Update task
- Delete task
- SQLite persistence (via Docker volume)


Project Structure

app/
 ├── main.py
 └── db/
     └── database.py
Dockerfile
docker-compose.yml
requirements.txt
.env.example


Run with Docker (Recommended)

cp .env.example .env
docker compose up --build
API will be available at:
http://localhost:8000

Swagger UI:
http://localhost:8000/docs

Stop container:
docker compose down


Run Locally (Without Docker)

Create virtual environment:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create environment file:
cp .env.example .env

Run server:
uvicorn app.main:app --reload

API Endpoints

GET /tasks → List all tasks
POST /tasks → Create new task
GET /tasks/{id} → Get task by ID
PUT /tasks/{id} → Update task
DELETE /tasks/{id} → Delete task

Example Request

Create task:
curl -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Buy milk"}'

Environment Variables (.env.example)

APP_PORT=8000
DATABASE_URL=sqlite:////data/todo.db

Note:
	•	.env is ignored by git
	•	Database file is stored inside Docker volume


Why This Project?

This project demonstrates:
	•	REST API design
	•	CRUD operations
	•	Database integration with SQLAlchemy
	•	Environment configuration with dotenv
	•	Docker containerization
	•	Clean backend structure

⸻

Author

Hesam Shahbazi
