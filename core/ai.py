from memory import memory
from memory.memory import MemoryManager
from core.prompt_builder import PromptBuilder
from core.client import client, MODEL
from memory.memory_service import MemoryService
from tools.tool_manager import ToolManager
from tools.registry import register_tools
from tools.tool_executor import ToolExecutor
from core.tool_decision import ToolDecision


class AI:

    def __init__(self):

        self.memory = MemoryManager()
        self.prompt_builder = PromptBuilder()
        self.memory_service = MemoryService()

        # sistema de herramientas
        self.tool_manager = ToolManager()

        register_tools(self.tool_manager)

        self.tool_executor = ToolExecutor(self.tool_manager)

        self.tool_decision = ToolDecision()
        


        self.messages = []

        self.SYSTEM_PROMPT = (
            "Tu nombre es Nova. "
            "Eres una compañera virtual amable, divertida y natural. "
            "Responde de forma breve y conversacional."
        )
        

    def chat(self, user_message: str):



        decision = self.tool_decision.decide(user_message)

        if decision.get("use_tool"):

            tool_call = {
                "tool": decision.get("tool"),
                "arguments": decision.get("arguments", {})
            }

            import json

            result = self.tool_executor.execute(
                json.dumps(tool_call)
            )

            user_message = (
                f"{user_message}\n\n"
                f"Resultado de la herramienta:\n"
                f"{result}"
            )



        self.messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        messages = self.prompt_builder.build(
            system_prompt=self.SYSTEM_PROMPT,
            memories=self.memory.load_memories(),
            history=self.messages
        )


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
    

    
        
    

    def process_user_message(self, message: str):

        self.memory_service.process_message(message)

        return self.chat(message)
    