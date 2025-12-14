from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import Base, engine
from app.db.deps import get_db
from app.schemas.job import JobCreateRequest, JobResponse
from app.services.job_service import create_job
from app.models import job  # ensures model registration


app = FastAPI(title=settings.app_name)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/jobs", response_model=JobResponse)
def create_job_endpoint(
    request: JobCreateRequest,
    db: Session = Depends(get_db),
):
    job = create_job(db, request.payload)
    return job

