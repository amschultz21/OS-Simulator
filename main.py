from job import Job
from scheduler import Scheduler
from memory_manager import MemoryManager
import random
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OS Simulator: Choose Scheduling Algorithm")
    parser.add_argument('--algorithm', type=str, default="FCFS", choices=["FCFS", "SJF"], help="Scheduling algorithm to use")
    args = parser.parse_args()

    total_memory = 1024
    memory_manager = MemoryManager(total_memory)
    scheduler = Scheduler(algorithm=args.algorithm)

    # Create random jobs
    for i in range(5):
        burst_time = random.randint(1, 5)
        memory_required = random.randint(100, 300)
        job = Job(i, burst_time, memory_required)
        scheduler.add_job(job)

    print(f"\n[INFO] Running Scheduler with algorithm: {args.algorithm}\n")
    memory_manager.display()
    scheduler.run(memory_manager)
    memory_manager.display()
