class ToolManager:

    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool

    def get_tool(self, name):
        return self.tools.get(name)

    def list_tools(self):
        return list(self.tools.values())

    def execute(self, name, **kwargs):

        tool = self.get_tool(name)

        if tool is None:
            raise ValueError(
                f"La herramienta '{name}' no existe."
            )

        return tool.execute(**kwargs)