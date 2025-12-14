from fastapi import FastAPI

from app.core.config import settings
from app.db.session import engine, Base
from app.models import job


app = FastAPI(title=settings.app_name)

@app.on_event("startup")
def on_startup():
    # Create database tables
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

