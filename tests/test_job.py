import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from job import Job

def test_job_initialization():
    job = Job(1, 3, 200)
    assert job.job_id == 1
    assert job.burst_time == 3
    assert job.memory_required == 200
