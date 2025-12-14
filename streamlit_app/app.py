import streamlit as st
import json
import requests

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="Workflow Processing Dashboard")

st.title("Workflow Processing Dashboard")

st.subheader("Submit New Job")

job_type = st.text_input(
    "Job Type / Name",
    placeholder="e.g. email notification, send password reset, set alert, quality check"
)

payload_text = st.text_area(
    "Job Payload (JSON)",
    placeholder='{"user_id": 123, "source": "upload", "priority": "high"}',
    height=150
)

if st.button("Submit Job"):
    if not job_type:
        st.error("Job type is required.")
    else:
        try:
            payload = json.loads(payload_text) if payload_text else {}
            payload["job_type"] = job_type

            response = requests.post(
                f"{API_BASE}/jobs",
                json={"payload": payload},
                timeout=5
            )

            if response.status_code == 201:
                st.success("Job submitted successfully")
                st.json(response.json())
            else:
                st.error(f"Error submitting job: {response.text}")

        except json.JSONDecodeError:
            st.error("Payload must be valid JSON")
