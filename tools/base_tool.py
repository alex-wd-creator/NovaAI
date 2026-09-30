class BaseTool:

    name = "base"
    description = "Herramienta base"

    def execute(self, **kwargs):
        raise NotImplementedError(
            "La herramienta debe implementar execute()"
        )