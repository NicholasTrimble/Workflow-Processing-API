import json
from sqlalchemy.orm import Session

from app.models.job import Job

def create_job(db: Session, payload: dict) -> Job:
    job = Job(
        input_payload=json.dumps(payload)
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job
