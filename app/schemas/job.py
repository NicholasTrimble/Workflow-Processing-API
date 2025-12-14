from datetime import datetime
from pydantic import BaseModel, Field
from app.models.job import JobStatus


class JobCreateRequest(BaseModel):
    payload: dict = Field(default_factory=dict)

class JobResponse(BaseModel):
    id: int
    status: JobStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

        