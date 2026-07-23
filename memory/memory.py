from memory.database import get_connection
from memory.rules import MEMORY_RULES

class MemoryManager:

    def save_memory(self, category: str, value: str) -> None:

        conn = get_connection()
        cursor = conn.cursor()

        rule = MEMORY_RULES.get(
            category,
            {"multiple": True}
        )

        if not rule["multiple"]:
            cursor.execute(
                "DELETE FROM memories WHERE category = ?",
                (category,)
            )

        cursor.execute(
            "INSERT INTO memories (category, value) VALUES (?, ?)",
            (category, value)
        )

        conn.commit()
        conn.close()

    def load_memories(self) -> list[tuple[str, str]]:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT category, value
            FROM memories
            ORDER BY id DESC
            LIMIT 20
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows