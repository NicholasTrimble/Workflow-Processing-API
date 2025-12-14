import json
from sqlalchemy.orm import Session
from app.models.job import Job, JobStatus
from datetime import datetime


def start_job(db: Session, job_id: int) -> Job | None:
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return None
    
    if job.status != JobStatus.queued:
        return job
    
    job.status = JobStatus.running
    job.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(job)

    return job


def create_job(db: Session, payload: dict) -> Job:
    job = Job(
        input_payload=json.dumps(payload),
        status=JobStatus.queued
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job


def get_job(db: Session, job_id: int) -> Job | None:
    return db.query(Job).filter(Job.id == job_id).first()


def get_job_by_id(db: Session, job_id: int) -> Job | None:
    return db.query(Job).filter(Job.id == job_id).first()


def list_jobs(db: Session, limit: int = 50, offset: int = 0) -> list[Job]:
    return (
        db.query(Job)
        .order_by(Job.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
