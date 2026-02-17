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

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Docker / Docker Compose

---

## Run Locally (without Docker)

### 1) Create venv & install dependencies
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt