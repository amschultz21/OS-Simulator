# OS Simulator: Memory Management & Job Scheduling in Linux

## 📚 Overview
This project is a Python-based operating system simulator designed to demonstrate key concepts in **Memory Management** and **Job Scheduling**. It simulates how an OS allocates memory to jobs and schedules them for execution using standard algorithms.

Developed to fulfill a course requirement in Operating Systems, this project applies real-world OS principles in a simplified, visualizable way.

---

## 🧠 Features

### ✅ Memory Management
- Simulated memory using fixed-size memory blocks.
- Dynamic allocation and deallocation of memory for jobs.
- Tracks fragmentation and merges free blocks on deallocation.
- `available_memory` property to monitor free space.

### ✅ Job Scheduling
- Implements **First-Come, First-Served (FCFS)** scheduling.
- Handles job burst time and memory requirements.
- Simulates job execution with Python's `multiprocessing`.

### ✅ Process Simulation
- Uses `multiprocessing.Process` to simulate separate jobs.
- Logs job execution start and end times.

---

## 🔧 How to Run

### Requirements
- Python 3.8+
- Linux/macOS system (or WSL for Windows)

### Setup
```bash
git clone https://github.com/yourusername/os-simulator.git
cd os-simulator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### Run the Simulation
python main.py

### Run Tests
pytest