# --- scheduler.py ---

from queue import Queue, PriorityQueue
import time
import multiprocessing

class Scheduler:
    def __init__(self, algorithm='FCFS'):
        self.algorithm = algorithm
        if algorithm == 'SJF':
            self.queue = PriorityQueue()
        else:
            self.queue = Queue()

    def add_job(self, job):
        if self.algorithm == 'SJF':
            self.queue.put((job.burst_time, job.job_id, job))  # Tiebreaker with job_id
        else:
            self.queue.put(job)

    def get_next_job(self):
        if self.queue.empty():
            return None
        if self.algorithm == 'SJF':
            return self.queue.get()[2]  # Extract the Job object
        return self.queue.get()

    def run(self, memory_manager):
        while not self.queue.empty():
            job = self.get_next_job()
            if memory_manager.allocate(job.job_id, job.memory_required):
                print(f"[Scheduler] Allocated memory for Job {job.job_id}")
                process = multiprocessing.Process(target=job.run)
                process.start()
                process.join()
                memory_manager.deallocate(job.job_id)
                print(f"[Scheduler] Deallocated memory for Job {job.job_id}")
            else:
                print(f"[Scheduler] Not enough memory for Job {job.job_id}, skipping...")
