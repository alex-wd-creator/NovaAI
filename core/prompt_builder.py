class PromptBuilder:

    def build(self, system_prompt: str, memories: list, history: list) -> list:
        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        if memories:
            lines = ["Información conocida sobre el usuario:"]
            for category, value in memories:
                lines.append(f"- {category}: {value}")

            memory_context = "\n".join(lines)

            messages.append({
                "role": "system",
                "content": memory_context
            })

        messages.extend(history)
        return messages

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