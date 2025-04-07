import time
import random

class Job:
    def __init__(self, job_id, burst_time, memory_required):
        self.job_id = job_id
        self.burst_time = burst_time
        self.memory_required = memory_required

    def run(self):
        print(f"[Job {self.job_id}] Started, running for {self.burst_time} seconds...")
        time.sleep(self.burst_time)
        print(f"[Job {self.job_id}] Finished.")
