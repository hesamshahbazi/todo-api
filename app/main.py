from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes.tasks import router as tasks_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(tasks_router)