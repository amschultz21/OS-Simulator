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
- Supports **First-Come, First-Served (FCFS)** and **Shortest Job First (SJF)** algorithms.
- Handles job burst time and memory requirements.
- Simulates job execution with Python's `multiprocessing`.
- Select algorithm via command-line: `--algorithm FCFS` or `--algorithm SJF`.

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
```

### Run the Simulation
```bash
python main.py --algorithm FCFS
python main.py --algorithm SJF
```

---

## 🧪 Running Tests
Unit tests are included using `pytest`.

```bash
pytest
```

Or to test with environment path:

```bash
PYTHONPATH=. pytest
```

---

## 🗂 Project Structure

```
os_simulator/
├── job.py                 # Job class definition
├── memory_manager.py      # Memory allocation logic
├── scheduler.py           # Job scheduler logic
├── main.py                # Simulation entry point
├── tests/                 # Unit tests
│   ├── test_job.py
│   └── test_memory_manager.py
├── requirements.txt
└── README.md
---

## 👨‍💻 Contributors
- Ayana Schultz
