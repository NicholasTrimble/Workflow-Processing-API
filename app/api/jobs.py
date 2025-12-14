from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.job import JobCreateRequest, JobResponse
from app.services.job_service import create_job, get_job_by_id, list_jobs, start_job
from app.models.job import JobStatus


router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post(
    "",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED,
)
def submit_job(
    request: JobCreateRequest,
    db: Session = Depends(get_db),
):
    job = create_job(db=db, payload=request.payload)
    return job


@router.get("/{job_id}", response_model=JobResponse)
def read_job(job_id: int, db: Session = Depends(get_db)):
    job = get_job_by_id(db=db, job_id=job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return job

@router.get("", response_model=list[JobResponse])
def list_all_jobs(
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    jobs = list_jobs(db=db, limit=limit, offset=offset)
    return jobs


@router.post("/{job_id}/start", response_model=JobResponse)
def start_job_endpoint(
    job_id: int,
    db: Session = Depends(get_db),
):
    job = start_job(db=db, job_id=job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if job.status != JobStatus.running:
        raise HTTPException(
            status_code=400,
            detail="Job cannot be started in its current state",
        )

    return job
