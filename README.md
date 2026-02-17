# 🚀 Todo API  
### FastAPI + SQLAlchemy + SQLite + Docker

A production-ready CRUD REST API built with FastAPI.  
Fully Dockerized and structured with clean backend architecture.

---

## 📌 Features

- Create task
- List all tasks
- Get task by ID
- Update task
- Delete task
- SQLite persistence (Docker volume)
- Environment configuration (.env)

---

## 🧱 Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Docker
- Docker Compose

---

## 📂 Project Structure

```
app/
 ├── main.py
 └── db/
     └── database.py

Dockerfile
docker-compose.yml
requirements.txt
.env.example
README.md
```

---

# 🐳 Run with Docker (Recommended)

### 1️⃣ Create environment file

```bash
cp .env.example .env
```

### 2️⃣ Build & Start container

```bash
docker compose up --build
```

API will be available at:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

### Stop container

```bash
docker compose down
```

---

# 💻 Run Locally (Without Docker)

### 1️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create environment file

```bash
cp .env.example .env
```

### 4️⃣ Run server

```bash
uvicorn app.main:app --reload
```

---

# 📡 API Endpoints

| Method | Endpoint        | Description        |
|--------|-----------------|--------------------|
| GET    | /tasks          | List all tasks     |
| POST   | /tasks          | Create new task    |
| GET    | /tasks/{id}     | Get task by ID     |
| PUT    | /tasks/{id}     | Update task        |
| DELETE | /tasks/{id}     | Delete task        |

---

# 🧪 Example Request

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk"}'
```

---

# 🔐 Environment Variables (.env.example)

```
APP_PORT=8000
DATABASE_URL=sqlite:///data/todo.db
```

Note:
- `.env` is ignored by git
- Database file is stored in Docker volume

---

# 🎯 Why This Project?

This project demonstrates:

- REST API design
- CRUD operations
- Database integration with SQLAlchemy
- Environment configuration
- Docker containerization
- Clean backend structure

---

## 👨‍💻 Author

Hesam Shahbazi