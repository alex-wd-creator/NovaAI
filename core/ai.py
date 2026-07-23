from core.memory_extractor import MemoryExtractor
from memory import memory
from memory.memory import MemoryManager

from core.client import client, MODEL


class AI:

    def __init__(self):

        self.memory = MemoryManager()
        self.extractor = MemoryExtractor()


        self.messages = [
            {
                "role": "system",
                "content": (
                    "Tu nombre es Chara. "
                    "Eres una compañera virtual amable, divertida y natural. "
                    "Responde de forma breve y conversacional."
                )
            }
        ]
        

    def chat(self, user_message: str):

        self.messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        messages = self.messages.copy()

        context = self.build_memory_context()

        if context:
            messages[0]["content"] += "\n\n" + context

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        answer = response.choices[0].message.content

        self.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        return answer
    
    def should_save_memory(self, text: str) -> bool:

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Decide si el siguiente mensaje contiene información "
                        "que sería útil recordar sobre el usuario a largo plazo.\n\n"
                        "Responde únicamente SI o NO."
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        answer = response.choices[0].message.content.strip().upper()

        return answer.startswith("SI")
    
        
    

    def process_user_message(self, message: str):

        should_save = self.should_save_memory(message)
        
        if should_save:

            memories = self.extractor.extract(message)

            for memory in memories:

                self.memory.save_memory(
                    memory["category"],
                    memory["value"]
                )

        return self.chat(message)
    
    def build_memory_context(self) -> str:

        memories = self.memory.load_memories()

        if not memories:
            return ""

        lines = [
            "Información conocida sobre el usuario."
        ]

        for category, value in memories:
            lines.append(f"- {category}: {value}")

        lines.append("")
        lines.append(
            "Cuando el usuario pregunte sobre sí mismo, "
            "usa esta información para responder."
        )

        return "\n".join(lines)