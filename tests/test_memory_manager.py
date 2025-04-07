import pytest
from memory_manager import MemoryManager

def test_allocation_deallocation():
    mm = MemoryManager(1024)
    assert mm.allocate("job1", 200) == True
    assert mm.allocate("job2", 900) == False  # not enough memory
    mm.deallocate("job1")
    assert mm.available_memory == 1024
