from memory.memory import MemoryManager
from core.memory_extractor import MemoryExtractor


class MemoryService:

    def __init__(self):
        self.manager = MemoryManager()
        self.extractor = MemoryExtractor()

    def process_message(self, message: str):
        result = self.extractor.extract(message)

        if not result.get("should_save"):
            return

        for memory in result.get("memories", []):
            self.manager.save_memory(
                memory["category"],
                memory["value"]
            )