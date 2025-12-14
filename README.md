Workflow Processing API

This project is a Python-based backend service for submitting, tracking, and managing asynchronous workflow jobs. It models a common backend pattern where work is accepted, queued, and processed over time instead of being handled immediately, allowing systems to remain responsive while long-running or failure-prone tasks are executed safely. The API exposes endpoints for job creation, status tracking, and lifecycle management, with a lightweight Streamlit interface included for manual submission and monitoring.


Features
Submit workflow jobs with structured input payloads
Track job status through defined lifecycle states (queued, running, completed, failed)
Retrieve individual jobs or list recent jobs with pagination
Lightweight Streamlit UI for interacting with the API without external tooling

Running the Project

Create and activate a virtual environment, then install dependencies:
pip install -r requirements.txt

Start the API server:
uvicorn app.main:app --reload

The API will be available at:
http://127.0.0.1:8000



Create a job:

POST /jobs
Content-Type: application/json

{
  "payload": {
    "job_type": "data_export",
    "requested_by": "system_user",
    "parameters": {
      "format": "csv",
      "range": "last_30_days"
    }
  }
}


Retrieve a job by ID:
GET /jobs/{job_id}

List recent jobs:
GET /jobs?limit=10&offset=0

Start processing a job:
POST /jobs/{job_id}/start


Streamlit Interface: how to run
streamlit run streamlit_app/app.py

