from job import Job
from scheduler import Scheduler
from memory_manager import MemoryManager
import random

if __name__ == "__main__":
    total_memory = 1024
    memory_manager = MemoryManager(total_memory)
    scheduler = Scheduler(algorithm="FCFS")

    # Create random jobs
    for i in range(5):
        burst_time = random.randint(1, 5)
        memory_required = random.randint(100, 300)
        job = Job(i, burst_time, memory_required)
        scheduler.add_job(job)

    memory_manager.display()
    scheduler.run(memory_manager)
    memory_manager.display()