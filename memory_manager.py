class MemoryBlock:
    def __init__(self, start, size, job_id=None):
        self.start = start
        self.size = size
        self.job_id = job_id

class MemoryManager:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.free_blocks = [MemoryBlock(0, total_memory)]
        self.allocated_blocks = []

    @property
    def available_memory(self):
        return sum(block.size for block in self.free_blocks)

    def allocate(self, job_id, size):
        for block in self.free_blocks:
            if block.size >= size:
                new_block = MemoryBlock(block.start, size, job_id)
                self.allocated_blocks.append(new_block)
                block.start += size
                block.size -= size
                if block.size == 0:
                    self.free_blocks.remove(block)
                return True
        return False

    def deallocate(self, job_id):
        to_remove = None
        for block in self.allocated_blocks:
            if block.job_id == job_id:
                self.free_blocks.append(MemoryBlock(block.start, block.size))
                to_remove = block
                break
        if to_remove:
            self.allocated_blocks.remove(to_remove)
            self._merge_free_blocks()

    def _merge_free_blocks(self):
        self.free_blocks.sort(key=lambda b: b.start)
        merged = []
        for block in self.free_blocks:
            if merged and merged[-1].start + merged[-1].size == block.start:
                merged[-1].size += block.size
            else:
                merged.append(block)
        self.free_blocks = merged

    def display(self):
        print("Allocated Memory:")
        for block in self.allocated_blocks:
            print(f"  Job {block.job_id}: {block.size} units at {block.start}")
        print("Free Memory:")
        for block in self.free_blocks:
            print(f"  Free block: {block.size} units at {block.start}")