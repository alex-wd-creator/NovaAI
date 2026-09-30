import json


class ToolExecutor:

    def __init__(self, tool_manager):
        self.tool_manager = tool_manager

    def execute(self, tool_call):

        try:
            data = json.loads(tool_call)

            tool_name = data["tool"]
            arguments = data.get("arguments", {})

            return self.tool_manager.execute(
                tool_name,
                **arguments
            )

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            return f"Error al ejecutar la herramienta: {e}"