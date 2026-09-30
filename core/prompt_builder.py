class PromptBuilder:

    def build(self, system_prompt: str, memories: list, history: list) -> list:

        prompt = system_prompt

        if memories:
            prompt += "\n\nInformación conocida sobre el usuario:"

            for category, value in memories:
                prompt += f"\n- {category}: {value}"

            prompt += (
                "\n\nCuando el usuario pregunte sobre sí mismo, "
                "usa esta información para responder."
            )

        messages = [
            {
                "role": "system",
                "content": prompt
            }
        ]

        messages.extend(history)

        return messages